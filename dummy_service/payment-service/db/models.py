from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, JSON
from db.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(String, unique=True)
    status = Column(String)
    amount = Column(Integer)
    created_at = Column(
    DateTime,
    default=datetime.utcnow
)

class ServiceEvent(Base):
    __tablename__ = "service_events"

    id = Column(Integer, primary_key=True)

    service_name = Column(String)

    event_type = Column(String)

    severity = Column(String)

    message = Column(Text)

    event_metadata = Column(JSON)

    created_at = Column(
    DateTime,
    default=datetime.utcnow
)
    



class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True)

    incident_id = Column(String, unique=True)

    alert_name = Column(String)

    severity = Column(String)

    service = Column(String)

    status = Column(String)

    alert_payload = Column(JSON)

    created_at = Column(DateTime)

    updated_at = Column(DateTime)