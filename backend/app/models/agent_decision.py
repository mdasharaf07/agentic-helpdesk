from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float
from sqlalchemy.sql import func
from app.db.config import Base

class AgentDecision(Base):
    __tablename__ = "agent_decisions"
    
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)
    agent_name = Column(String, nullable=False)
    decision_type = Column(String, nullable=False)
    decision_output = Column(Text, nullable=False)
    confidence_score = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
