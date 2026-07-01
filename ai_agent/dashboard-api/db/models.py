from sqlalchemy import Column, Integer, String, DateTime, Text, JSON, Float
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

#store LLM result data
class InvestigationResult(Base):
    __tablename__ = "investigation_results"

    id = Column(Integer, primary_key=True)

    incident_id = Column(String)

    root_cause = Column(Text)

    confidence = Column(Float)

    severity = Column(String)

    recommendations = Column(JSON)

    evidence_summary = Column(JSON)

    status = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

#status 
# OPEN

# INVESTIGATING

# ANALYZED

# WAITING_HUMAN

# RESOLVED

# FAILED