from datetime import datetime
from pydantic import BaseModel


class IssueCreate(BaseModel):
    title: str
    description: str
    priority: str


class IssueUpdate(BaseModel):
    status: str


class IssueResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str
    # user_id: int - Implement after user auth available.
    created_at: datetime

    class Config:
        from_attributes = True
