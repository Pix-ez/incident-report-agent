from sqlalchemy import Column, Integer, String, DateTime, Text, JSON
from datetime import datetime

from db.database import Base


class Incident(Base):

    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True)

    incident_id = Column(String, unique=True)

    alert_name = Column(String)

    severity = Column(String)

    status = Column(String)

    service = Column(String)

    alert_payload = Column(JSON)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class Investigation(Base):
    __tablename__ = "investigations"

    id = Column(Integer, primary_key=True)

    incident_id = Column(String)

    status = Column(String)

    metrics_data = Column(JSON)

    logs_data = Column(JSON)

    historical_events = Column(JSON)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )