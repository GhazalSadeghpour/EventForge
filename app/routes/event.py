from fastapi import APIRouter, status, Depends, HTTPException
from app.schemas.event import EventOut, EventCreate

from sqlalchemy.orm import Session

from app.db import get_db
from app.models.event import Event

router = APIRouter(prefix="/events", tags=["events"])

@router.post("", response_model=EventOut, status_code=status.HTTP_201_CREATED)
def create_event(event: EventCreate, db: Session = Depends(get_db)) -> EventOut:
    
    db_event = Event(**event.model_dump())
    
    db.add(db_event)
    db.commit()

    db.refresh(db_event)
    return db_event

@router.get("", response_model=list[EventOut])
def list_events(db: Session = Depends(get_db)) -> list[EventOut]:
    events = db.query(Event).order_by(Event.created_at.desc()).limit(50).all()
    return events
