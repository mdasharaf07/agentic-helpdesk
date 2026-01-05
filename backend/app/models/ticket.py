from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.config import Base

class Ticket(Base):
    __tablename__ = "tickets"
    
    pass
