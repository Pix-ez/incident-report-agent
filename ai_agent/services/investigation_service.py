from  db.database import SessionLocal

from  db.models import (
    Incident,
    Investigation
)

from  clients.prometheus_client import (
    PrometheusClient
)

from  clients.loki_client import (
    LokiClient
)


prom = PrometheusClient()

loki = LokiClient()

ALERT_MAPPING = {

    "HighPaymentFailureRate": {

        "metrics": [
            "payment_failures_total",
            "http_requests_total"
        ],

        "log_query":
        '{job="docker"} |= "payment_failed"'
    },

    "HighLatency": {

        "metrics": [
            "http_request_latency_seconds_count"
        ],

        "log_query":
        '{job="docker"} |= "timeout"'
    },

    "ServiceDown": {

        "metrics": [
            "up"
        ],

        "log_query":
        '{job="docker"}'
    }
}

def investigate_incident(
    incident_id: str
):

    db = SessionLocal()

    incident = (
        db.query(Incident)
        .filter(
            Incident.incident_id == incident_id
        )
        .first()
    )

    if not incident:
        return

    config = ALERT_MAPPING.get(
        incident.alert_name
    )

    metrics = {}

    for metric in config["metrics"]:

        metrics[metric] = (
            prom.query(metric)
        )

    logs = loki.query(
        config["log_query"]
    )

    historical_events = []

    investigation = Investigation(

        incident_id=incident_id,

        status="READY_FOR_ANALYSIS",

        metrics_data=metrics,

        logs_data=logs,

        historical_events=historical_events
    )

    db.add(investigation)

    incident.status = (
        "READY_FOR_ANALYSIS"
    )

    db.commit()

    db.close()