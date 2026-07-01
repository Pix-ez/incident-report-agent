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

router = APIRouter()


@router.get(
    "/investigations/{incident_id}"
)

def get_investigation(

    incident_id,

    db: Session = Depends(get_db)

):

    repo = IncidentRepository(db)

    investigation = repo.get_investigation(
        incident_id
    )

    if not investigation:

        raise HTTPException(
            404,
            "Not found"
        )

    return investigation


@router.get(
    "/analysis/{incident_id}"
)

def get_analysis(

    incident_id,

    db: Session = Depends(get_db)

):

    repo = IncidentRepository(db)

    result = repo.get_analysis(
        incident_id
    )

    if not result:

        raise HTTPException(
            404,
            "Not found"
        )

    return result