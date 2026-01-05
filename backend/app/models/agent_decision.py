from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.config import Base

class AgentDecision(Base):
    __tablename__ = "agent_decisions"
    
    pass
