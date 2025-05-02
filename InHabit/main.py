from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from models import Habit, HabitCreate, HabitResponse, HabitLog, HabitLogBase, get_db

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
async def log_habit(
    habit_id: int, habit_log: HabitLogBase, db: Session = Depends(get_db)
):
    # TODO: Implement HabitLog logic - inserts new row with today's date and habit ID, cannot log more than once per day
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    db_habit_log = HabitLog(
        id=habit_log.id,
    )
    db.add(db_habit_log)
    db.commit()
    db.refresh(db_habit_log)
    return db_habit_log
    # return {"message": "Habit logged for today!"}
    # TODO: Return 404 if logging habit that doesn't exist


@app.get("/habits/{habit_id}/streak")
async def get_habit_streak():
    # TODO: Implement streak request logic with HabitLog - return count of consecutive days recorded (including today) from HabitLog
    # TODO: Return 404 if checking habit streak that doesn't exist
    return {"message": "I will get the current completion streak for a habit!"}
