from pydantic import BaseModel
from datetime import datetime
from app.models.enums import TicketStatus, TicketPriority
from typing import Optional

class TicketCreate(BaseModel):
    title: str
    description: str
    category: str
    priority: TicketPriority

class TicketUpdate(BaseModel):
    status: TicketStatus
    priority: Optional[TicketPriority] = None

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    priority: TicketPriority
    status: TicketStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True