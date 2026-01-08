from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.config import get_db
from app.models.ticket import Ticket
from app.models.enums import TicketStatus
from app.schemas.ticket import TicketCreate, TicketResponse, TicketUpdate

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/", response_model=TicketResponse)
async def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        category=ticket.category,
        priority=ticket.priority,
        status=TicketStatus.NEW
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.get("/", response_model=List[TicketResponse])
async def list_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).order_by(Ticket.created_at.desc()).all()
    return tickets

@router.get("/{ticket_id}", response_model=TicketResponse)
async def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

def validate_status_transition(current_status: TicketStatus, new_status: TicketStatus) -> bool:
    """Lightweight state transition validation"""
    # NEW → IN_PROGRESS
    if current_status == TicketStatus.NEW and new_status == TicketStatus.IN_PROGRESS:
        return True
    # IN_PROGRESS → RESOLVED
    if current_status == TicketStatus.IN_PROGRESS and new_status == TicketStatus.RESOLVED:
        return True
    # ANY → ESCALATED
    if new_status == TicketStatus.ESCALATED:
        return True
    # Same status (no change)
    if current_status == new_status:
        return True
    return False

@router.put("/{ticket_id}", response_model=TicketResponse)
async def update_ticket(ticket_id: int, ticket_update: TicketUpdate, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    # Validate status transition if status is being updated
    if ticket_update.status and ticket_update.status != ticket.status:
        if not validate_status_transition(ticket.status, ticket_update.status):
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid status transition from {ticket.status} to {ticket_update.status}"
            )
        ticket.status = ticket_update.status
    
    # Update priority if provided
    if ticket_update.priority is not None:
        ticket.priority = ticket_update.priority
    
    db.commit()
    db.refresh(ticket)
    return ticket
