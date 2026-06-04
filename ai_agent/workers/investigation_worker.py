import json
import redis

from services.investigation_service import (
    investigate_incident
)
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger("investigation-worker")


redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True,
    health_check_interval=30,
    socket_timeout=None,
    socket_connect_timeout=30
)
QUEUE_NAME = (
    "incident-investigation-queue"
)

while True:
    # pass

    incident_id = None

    try:

        result = redis_client.brpop(
            QUEUE_NAME,
            timeout=0
        )

        if not result:
            continue

        _, raw_message = result

        payload = json.loads(raw_message)

        incident_id = payload["incident_id"]

        logger.info(
            f"Investigating {incident_id}"
        )

        investigate_incident(
            incident_id
        )

        logger.info(
            f"Completed {incident_id}"
        )

    except Exception as e:

        logger.exception(
            f"Worker failed. Incident={incident_id}"
        )