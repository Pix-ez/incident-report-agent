from sqlalchemy import Column, Integer, String
from db.database import Base

class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    status = Column(String)

    amount = Column(Integer)    