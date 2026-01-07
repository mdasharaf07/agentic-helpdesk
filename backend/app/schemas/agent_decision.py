from pydantic import BaseModel
from datetime import datetime

class AgentDecisionCreate(BaseModel):
    ticket_id: int
    agent_name: str
    decision_type: str
    decision_output: str
    confidence_score: float

class AgentDecisionResponse(BaseModel):
    id: int
    ticket_id: int
    agent_name: str
    decision_type: str
    decision_output: str
    confidence_score: float
    created_at: datetime

    class Config:
        from_attributes = True