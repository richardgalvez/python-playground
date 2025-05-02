from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from models import Habit, HabitCreate, HabitResponse, get_db

app = FastAPI()


@app.post("/habits", response_model=HabitResponse)
async def create_habit(habit: HabitCreate, db: Session = Depends(get_db)):
    db_habit = Habit(
        name=habit.name,
        description=habit.description,
    )
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit


@app.get("/habits", response_model=List[HabitResponse])
async def get_habits(skip: int = 0, db: Session = Depends(get_db)):
    habits = db.query(Habit).offset(skip).all()
    return habits


@app.get("/habits/{habit_id}", response_model=HabitResponse)
async def get_habit(habit_id: int, db: Session = Depends(get_db)):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found.")
    return habit


@app.post("/habits/{habit_id}/log")
async def log_habit_completion():
    return {"message": "I will log today's completion for a habit!"}


@app.get("/habits/{habit_id}/streak")
async def get_habit_streak():
    return {"message": "I will get the current completion streak for a habit!"}

