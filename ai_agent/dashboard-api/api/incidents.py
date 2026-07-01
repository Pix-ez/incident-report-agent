from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from repositories.incident_repository import (
    IncidentRepository
)

from db.dependencies import get_db

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


@router.get("")
def list_incidents(

    db: Session = Depends(get_db)

):

    repo = IncidentRepository(db)

    return repo.list_incidents()


@router.get("/{incident_id}")
def get_incident(

    incident_id: str,

    db: Session = Depends(get_db)

):

    repo = IncidentRepository(db)

    incident = repo.get_incident(
        incident_id
    )

    if not incident:

        raise HTTPException(
            404,
            "Incident not found"
        )

    return incident


@router.patch("/{incident_id}/status")
def update_status(

    incident_id: str,

    payload: dict,

    db: Session = Depends(get_db)

):

    repo = IncidentRepository(db)

    return repo.update_status(

        incident_id,

        payload["status"]
    )