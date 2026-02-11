from fastapi import APIRouter, status
from app.schemas.event import EventOut, EventCreate

router = APIRouter(prefix="/events", tags=["events"])

@router.post("", response_model=EventOut, status_code=status.HTTP_202_ACCEPTED)
def create_event(event: EventCreate) -> EventOut:
    return EventOut(**event.model_dump())

@router.get("")
def list_events():
    return []
