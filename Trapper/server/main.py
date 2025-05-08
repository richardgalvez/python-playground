from fastapi import FastAPI

app = FastAPI()

# TODO: User Authentication - 5 routes

# TODO: Issue Management - All actions must be scoped to the current user


@app.get("/")
def home():
    return {"message": "Homepage with all issues for the logged-in user."}


@app.get("/report")
def new_issue():
    return {"message": "New issue form."}


@app.post("/report")
def create_issue():
    return {"message": "Create new issue for current user."}


@app.get("/issues/{id}")
def get_issues():
    return {"message": "View issue detail page."}


@app.post("/issues/{id}/resolve")
def resolve_issue():
    return {"message": "Mark an issue as resolved."}
