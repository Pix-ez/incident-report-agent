# repositories/investigation_repository.py

from db.database import SessionLocal
from db.models import (
    Investigation,
    InvestigationResult
)


def get_investigation(
    incident_id: str
):

    db = SessionLocal()

    try:

        return (
            db.query(Investigation)
            .filter(
                Investigation.incident_id
                == incident_id
            )
            .first()
        )

    finally:

        db.close()


def save_analysis_result(
    result: InvestigationResult
    ):

    db = SessionLocal()

    try:

        db.add(result)

        db.commit()

        db.refresh(result)

        return result

    finally:

        db.close()