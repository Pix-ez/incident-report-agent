from sqlalchemy import Column, Integer, String, DateTime, Text, JSON
from db.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(String, unique=True)
    status = Column(String)
    amount = Column(Integer)
    created_at = Column(DateTime)

class ServiceEvent(Base):
    __tablename__ = "service_events"

    id = Column(Integer, primary_key=True)

    service_name = Column(String)

    event_type = Column(String)

    severity = Column(String)

    message = Column(Text)

    event_metadata = Column(JSON)

    created_at = Column(DateTime)