from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime

DATABASE_URL = "sqlite:///./inhabit.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Habit(Base):
    __tablename__ = "habit"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now)


class HabitLog(Base):
    __tablename__ = "habit_log"
    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habit.id"))
    logged_date = Column(DateTime, default=datetime.now)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class HabitCreate(BaseModel):
    name: str
    description: str


# Pydantic schemas that defines the structure of the data for validation.
class HabitResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True


class HabitLogBase(BaseModel):
    id: int
    hait_id: int

    class Config:
        from_attributes = True
