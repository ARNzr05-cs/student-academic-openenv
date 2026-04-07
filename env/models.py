from pydantic import BaseModel
from typing import List, Dict, Optional


class Email(BaseModel):
    id: str
    subject: str
    body: str
    sender: str
    timestamp: str


class CalendarEvent(BaseModel):
    title: str
    date: str
    time: Optional[str] = None
    room: Optional[str] = None
    priority: int = 1


class Action(BaseModel):
    ignore: bool = False
    mark_important: bool = False
    extract_deadline: bool = False
    schedule: bool = False


class Reward(BaseModel):
    value: float
    reason: str


class Observation(BaseModel):
    unread_count: int
    current_email: Email
    calendar: List[CalendarEvent]
    extracted_entities: Dict[str, str]
    processed_count: int
    history: List[str]