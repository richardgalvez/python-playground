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
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    hashed_password: str
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: str
    id: int
