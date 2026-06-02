from db.database import SessionLocal
from db.models import ServiceEvent

def create_event(
    service_name: str,
    event_type: str,
    severity: str,
    message: str,
    event_metadata: dict = None
):
    db = SessionLocal()

    try:
        event = ServiceEvent(
            service_name=service_name,
            event_type=event_type,
            severity=severity,
            message=message,
            event_metadata=event_metadata or {}
        )

        db.add(event)
        db.commit()
    finally:
        db.close()
