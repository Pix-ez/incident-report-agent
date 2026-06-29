from sqlalchemy.orm import Session

from db.models import (
    Incident,
    Investigation,
    InvestigationResult
)


class IncidentRepository:

    def __init__(self, db: Session):

        self.db = db


    def list_incidents(self):

        return (
            self.db.query(Incident)
            .order_by(
                Incident.created_at.desc()
            )
            .all()
        )


    def get_incident(
        self,
        incident_id: str
    ):

        return (
            self.db.query(Incident)
            .filter(
                Incident.incident_id == incident_id
            )
            .first()
        )


    def get_investigation(
        self,
        incident_id: str
    ):

        return (
            self.db.query(Investigation)
            .filter(
                Investigation.incident_id == incident_id
            )
            .first()
        )


    def get_analysis(
        self,
        incident_id: str
    ):

        return (
            self.db.query(
                InvestigationResult
            )
            .filter(
                InvestigationResult.incident_id
                == incident_id
            )
            .first()
        )


    def update_status(
        self,
        incident_id,
        status
    ):

        incident = self.get_incident(
            incident_id
        )

        incident.status = status

        self.db.commit()

        self.db.refresh(
            incident
        )

        return incident