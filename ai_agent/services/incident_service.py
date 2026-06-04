import uuid

from db.database import SessionLocal
from db.models import Incident


def create_incident(alert):

    db = SessionLocal()

    incident = Incident(

        incident_id=f"INC-{uuid.uuid4().hex[:8]}",

        alert_name=alert.labels.get(
            "alertname",
            "unknown"
        ),

        severity=alert.labels.get(
            "severity",
            "warning"
        ),

        service=alert.labels.get(
            "service",
            "unknown"
        ),

        status="OPEN",

        alert_payload=alert.model_dump()
    )

    db.add(incident)

    db.commit()

    db.refresh(incident)

    db.close()

    return incident