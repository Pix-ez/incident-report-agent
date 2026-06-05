

import json
import time
import redis

from db.models import (
    InvestigationResult
)

from db.helper import (
    get_investigation,
    save_analysis_result
)

from schemas.analysis import RCAResponse

from services.llm_service import (
    analyze_incident
)

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger("analysis-worker")

QUEUE_NAME = "analysis-queue"



redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True,
    health_check_interval=30,
    socket_timeout=None,
    socket_connect_timeout=30
)


def build_context(
    investigation
):

    return {

        "metrics": (
            investigation.metrics_data
            or {}
        ),

        "logs": (
            investigation.logs_data
            or []
        ),

        "historical_events": (
            investigation.historical_events
            or {}
        )
    }


def determine_status(
    result: RCAResponse
):

    if result.confidence < 0.75:
        return "WAITING_HUMAN"

    if result.severity.lower() == "critical":
        return "WAITING_HUMAN"

    return "ANALYZED"


def process_incident(
    incident_id: str
):

    investigation = get_investigation(
        incident_id
    )

    if not investigation:

        logger.error(
            f"No investigation found: {incident_id}"
        )

        return

    context = build_context(
        investigation
    )

    logger.info(
        f"Running RCA for {incident_id}"
    )

    llm_response = analyze_incident(
        context
    )

    parsed = RCAResponse(
        **llm_response
    )

    status = determine_status(
        parsed
    )

    result = InvestigationResult(

        incident_id=incident_id,

        root_cause=parsed.root_cause,

        confidence=parsed.confidence,

        severity=parsed.severity,

        recommendations=parsed.recommendations,

        evidence_summary=parsed.evidence_summary,

        status=status
    )

    save_analysis_result(
        result
    )

    logger.info(
        f"Analysis complete: {incident_id}"
    )


def start_worker():

    logger.info(
        "Analysis worker started"
    )

    while True:

        try:

            result = redis_client.brpop(
                QUEUE_NAME,
                timeout=0
            )

            if not result:
                continue

            _, raw_message = result

            payload = json.loads(
                raw_message
            )

            incident_id = payload[
                "incident_id"
            ]

            process_incident(
                incident_id
            )

        except Exception as e:

            logger.exception(
                f"Analysis worker error: {e}"
            )

            time.sleep(5)


if __name__ == "__main__":

    start_worker()