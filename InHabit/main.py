from sqlalchemy import desc
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
import datetime

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

    def log_habit():
        db_habit_log = HabitLog(habit_id=habit.id)
        db.add(db_habit_log)
        db.commit()
        db.refresh(db_habit_log)

    # Get current date in yyyy-mm-dd format to compare to the latest logged record, if it exists.
    current_date = datetime.datetime.now().date().isoformat()
    latest_record_query = (
        db.query(HabitLog)
        .filter(HabitLog.habit_id == habit_id)
        .order_by(desc(HabitLog.logged_date))
        .first()
    )
    if latest_record_query is None:
        log_habit()
        return {"message": "Marked Complete - Habit logged for today!"}
    else:
        logged_date = latest_record_query.logged_date.date().isoformat()
        if current_date == logged_date:
            raise HTTPException(
                status_code=422, detail="Habit completed today already."
            )
        else:
            log_habit()
            return {"message": "Marked Complete - Habit logged for today!"}


@app.get("/habits/{habit_id}/streak")
async def get_habit_streak(habit_id: int, db: Session = Depends(get_db)):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if habit is None:
        raise HTTPException(
            status_code=404, detail="Cannot check streak, habit not found."
        )
    # TODO: Implement streak request logic with HabitLog
    # Return count of a single habit's log
    log_count = db.query(HabitLog).filter(HabitLog.habit_id == habit_id).count()
    # Return count of consecutive days recorded (including today) from HabitLog
    # Logic = Must be within 24 hours of each other?
    current_time = datetime.datetime.now().date().isoformat()
    return log_count
    # return {"message": "I will get the current completion streak for a habit!"}
