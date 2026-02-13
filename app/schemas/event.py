from typing import Any, Dict
from uuid import UUID, uuid4
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class EventCreate(BaseModel):
    event_type: str = Field(..., min_length=1, max_length=100)
    source: str = Field(..., min_length=1, max_length=100)
    payload: Dict[str, Any]


class EventOut(EventCreate):
    model_config = ConfigDict(from_attributes = True) # to return SQLAlchey objects
    event_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
