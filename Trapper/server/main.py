from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.models import Base, engine, get_db, Issue
from db.schema import IssueCreate, IssueResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Initialize database tables on startup.
Base.metadata.create_all(bind=engine)

# TODO: Issue Management - All actions must be scoped to the current user


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    issues = db.query(Issue).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Trapper", "issues": issues}
    )


@app.get("/report")
async def new_issue():
    return {"message": "New issue form."}


@app.post("/report", response_model=IssueResponse)
async def create_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    db_issue = Issue(
        title=issue.title,
        description=issue.description,
        priority=issue.priority,
    )
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue


@app.get("/issues/{id}", response_model=IssueResponse)
async def get_issue(issue_id: int, db: Session = Depends(get_db)):
    issue = db.query(Issue).filter(Issue.id == issue_id).first()
    if issue is None:
        raise HTTPException(status_code=404, detail="Issue not found.")
    return issue


@app.post("/issues/{id}/resolve")
async def resolve_issue():
    # TODO: Add HTTPException if issue not found.
    return {"message": "Mark an issue as resolved."}
