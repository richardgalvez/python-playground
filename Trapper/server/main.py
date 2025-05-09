from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import desc
from sqlalchemy.orm import Session
from db.models import Base, engine, get_db, Issue
from db.schema import IssueCreate, IssueResponse
from typing import List

app = FastAPI()

# Initialize database tables on startup.
Base.metadata.create_all(bind=engine)

# TODO: Issue Management - All actions must be scoped to the current user


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
