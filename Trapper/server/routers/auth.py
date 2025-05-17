from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, Request, Response, status, Form
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import HTMLResponse, RedirectResponse
from jose import JWTError, jwt
from typing import Annotated
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from db.models import User, get_db, db_dependency
from db.schema import Token, TokenPayload

router = APIRouter(tags=["auth"])

SECRET_KEY = "cfa5a8a5191a9100bf97f53e091fcd6ebae8d55e3b87ee008c06a504a6eb7aeb"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")


# TODO: Check if username already exists, display message to use unique username if so
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(
    db: db_dependency, username: str = Form(...), password: str = Form(...)
):
    """
    Creates a new user with a hashed password and stores it in the database.
    """
    new_user = User(username=username, hashed_password=bcrypt_context.hash(password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return RedirectResponse("/", status_code=302)


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    """
    Verifies the username and password against stored hashed password.
    Returns the user if authentication is successful, otherwise returns False.
    """
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    """
    Generates a JWT access token with an expiration time.
    """
    encode = {"sub": username, "id": user_id}
    expires = datetime.now() + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(request: Request, db: db_dependency):
    """
    Decodes the JWT token and retrieves user details.
    Raises an exception if the token is invalid (details incorrect) or expired.
    """
    token = request.cookies.get("access_token")
    if not token:
        user_logged_in = False
        return user_logged_in
    try:
        payload_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Gather token's payload data in format of defined model to be assigned and checked.
        token_payload = TokenPayload(**payload_data)
        username = token_payload.sub
        user_id = token_payload.id
        # Guaranteed database check for user by referencing id from token's payload data.
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found - could not validate.",
            )
        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is unauthorized or not valid.",
        )


@router.post("/token", response_model=Token)
async def login_for_access_token(
    db: db_dependency, username: str = Form(...), password: str = Form(...)
):
    """
    Authenticates user credentials and returns a JWT token if valid.
    """
    user = authenticate_user(username, password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not authenticated."
        )
    username = user.username
    user_id = user.id
    token = create_access_token(username, user_id, timedelta(minutes=30))
    # Prepare to return a redirect and set a cookie with login info for session.
    response = RedirectResponse(url="/", status_code=302)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=1800,
    )
    return response


user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/logout", response_class=HTMLResponse)
async def logout(response: Response):
    response = RedirectResponse(url="/", status_code=302)
    response.delete_cookie("access_token")
    return response
