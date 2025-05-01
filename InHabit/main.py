from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to InHabit!"}


@app.get("/habits")
async def get_habits():
    return {"message": "I will list all habits!"}


@app.post("/habits")
async def create_habit():
    return {"message": "I will create a habit!"}


@app.get("/habits/{habit_id}")
async def get_habit_details():
    return {"message": "I will get details for a single habit!"}


@app.post("/habits/{habit_id}/log")
async def log_habit_completion():
    return {"message": "I will log today's completion for a habit!"}


@app.get("/habits/{habit_id}/streak")
async def get_habit_streak():
    return {"message": "I will get the current completion streak for a habit!"}
