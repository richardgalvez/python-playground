from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from models import (
    Habit,
    HabitCreate,
    HabitLog,
    HabitResponse,
    get_db,
)

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
async def log_habit(habit_id: int, db: Session = Depends(get_db)):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if habit is None:
        raise HTTPException(
            status_code=404, detail="Cannot be logged, habit not found."
        )
    # TODO: Check log for if: new day, else: error if already logged for the day
    # log_check = db.query(HabitLog).filter(Habit.id == habit_id)
    db_habit_log = HabitLog(habit_id=habit.id)
    db.add(db_habit_log)
    db.commit()
    db.refresh(db_habit_log)
    # return {"message": "Habit logged for today."}
    return db_habit_log  # Use for testing/checking result


@app.get("/habits/{habit_id}/streak")
async def get_habit_streak(habit_id: int, db: Session = Depends(get_db)):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if habit is None:
        raise HTTPException(
            status_code=404, detail="Cannot check streak, habit not found."
        )
    # TODO: Implement streak request logic with HabitLog
    # Return count of a single habit's log
    log_count = db.query(HabitLog).all()
    # Return count of consecutive days recorded (including today) from HabitLog
    # Logic = Must be within 24 hours of each other?
    return log_count
    # return {"message": "I will get the current completion streak for a habit!"}
