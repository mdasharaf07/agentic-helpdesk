from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from app.db.config import Base
from app.models.enums import TicketStatus, TicketPriority

class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    priority = Column(Enum(TicketPriority), nullable=False, default=TicketPriority.MEDIUM)
    status = Column(Enum(TicketStatus), nullable=False, default=TicketStatus.NEW)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
