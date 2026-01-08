from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.config import get_db
from app.models.agent_decision import AgentDecision
from app.schemas.agent_decision import AgentDecisionCreate, AgentDecisionResponse

router = APIRouter(prefix="/agent-decisions", tags=["Agent Decisions"])

@router.post("/", response_model=AgentDecisionResponse)
async def create_agent_decision(decision: AgentDecisionCreate, db: Session = Depends(get_db)):
    db_decision = AgentDecision(
        ticket_id=decision.ticket_id,
        agent_name=decision.agent_name,
        decision_type=decision.decision_type,
        decision_output=decision.decision_output,
        confidence_score=decision.confidence_score
    )
    db.add(db_decision)
    db.commit()
    db.refresh(db_decision)
    return db_decision

@router.get("/ticket/{ticket_id}", response_model=List[AgentDecisionResponse])
async def get_ticket_decisions(ticket_id: int, db: Session = Depends(get_db)):
    decisions = db.query(AgentDecision).filter(
        AgentDecision.ticket_id == ticket_id
    ).order_by(AgentDecision.created_at.asc()).all()
    return decisions
