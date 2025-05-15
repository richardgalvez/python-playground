from fastapi import FastAPI, Form, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.models import Base, engine, get_db, Issue
from routers import auth

app = FastAPI()


templates = Jinja2Templates(directory="templates")

# Initialize database tables on startup.
Base.metadata.create_all(bind=engine)


app.include_router(auth.router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    issues = db.query(Issue).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Trapper", "issues": issues}
    )


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/report", response_class=HTMLResponse)
async def new_issue(request: Request):
    return templates.TemplateResponse(
        "report.html", {"request": request, "title": "Trapper"}
    )


# TODO: Refactor to use the IssueCreate class?
@app.post("/report", response_class=RedirectResponse)
async def submit(
    title: str = Form(...),
    description: str = Form(...),
    priority: str = Form(...),
    db: Session = Depends(get_db),
):
    # TODO: Entered username to be converted to reference their id value
    db_issue = Issue(title=title, description=description, priority=priority)
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return RedirectResponse("/", status_code=302)


@app.get("/issues/{id}", response_class=HTMLResponse)
async def get_issue(id: int, request: Request, db: Session = Depends(get_db)):
    issue = db.query(Issue).filter(Issue.id == id).first()
    if issue is None:
        raise HTTPException(status_code=404, detail="Issue not found.")
    return templates.TemplateResponse(
        "issues.html", {"request": request, "title": "Trapper", "issue": issue}
    )


@app.post("/issues/{id}/resolve", response_class=RedirectResponse)
async def resolve_issue(
    id: int, issue_status: str = Form(...), db: Session = Depends(get_db)
):
    db_issue = db.query(Issue).filter(Issue.id == id).first()
    if not db_issue:
        raise HTTPException(status_code=404, detail="Issue not found.")

    db_issue.status = issue_status
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return RedirectResponse("/", status_code=302)
