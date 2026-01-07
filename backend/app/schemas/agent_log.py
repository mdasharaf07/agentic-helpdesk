from pydantic import BaseModel
from datetime import datetime

class AgentLogCreate(BaseModel):
    ticket_id: int
    agent_name: str
    log_level: str
    message: str

class AgentLogResponse(BaseModel):
    id: int
    ticket_id: int
    agent_name: str
    log_level: str
    message: str
    created_at: datetime

    class Config:
        from_attributes = True