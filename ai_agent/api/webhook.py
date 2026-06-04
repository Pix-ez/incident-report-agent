from fastapi import APIRouter

from schemas.alertmanager import AlertManagerPayload

from services.incident_service import create_incident

from services.queue_service import enqueue_incident

router = APIRouter()


@router.post("/webhook/alert")
def receive_alert(
    payload: AlertManagerPayload
):

    created = []

    for alert in payload.alerts:

        incident = create_incident(alert)

        enqueue_incident(
            incident.incident_id
        )

        created.append(
            incident.incident_id
        )

    return {
        "status": "accepted",
        "incidents": created
    }