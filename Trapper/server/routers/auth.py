from fastapi import APIRouter

router = APIRouter()

# TODO: User Authentication - Store user sessions using signed cookies or dependency injection


@router.get("/register")
def get_register():
    return {"message": "Registration form."}


@router.post("/register")
def create_user():
    return {"message": "Create user account."}


@router.get("/login")
def get_login():
    return {"message": "Login form."}


@router.post("/login")
def login_user():
    return {"message": "Authenticate user and start session."}


@router.get("/logout")
def logout():
    return {"message": "End session and redirect to homepage."}
