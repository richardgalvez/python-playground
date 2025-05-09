from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import desc
from sqlalchemy.orm import Session
from db.models import Base, engine, get_db, Issue
from db.schema import IssueCreate, IssueResponse
from typing import List

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Initialize database tables on startup.
Base.metadata.create_all(bind=engine)

# TODO: Issue Management - All actions must be scoped to the current user


@app.get("/view", response_class=HTMLResponse)
async def view(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "View Test"}
    )


@app.get("/", response_model=List[IssueResponse])
def home(db: Session = Depends(get_db)):
    issues = db.query(Issue).all()
    return issues


@app.get("/report")
def new_issue():
    return {"message": "New issue form."}


@app.post("/report", response_model=(IssueResponse))
def create_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    db_issue = Issue(
        title=issue.title,
        description=issue.description,
        priority=issue.priority,
    )
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue


@app.get("/issues/{id}")
def get_issues():
    return {"message": "View issue detail page."}


@app.post("/issues/{id}/resolve")
def resolve_issue():
    return {"message": "Mark an issue as resolved."}
