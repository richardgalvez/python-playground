from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from db.models import User, get_db, db_dependency
from db.schema import UserCreate, UserResponse

router = APIRouter(tags=["auth"])

SECRET_KEY = "cfa5a8a5191a9100bf97f53e091fcd6ebae8d55e3b87ee008c06a504a6eb7aeb"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")


# TODO: User Authentication - Store user sessions using signed cookies or dependency injection


def decode_token(token):
    return UserResponse(
        id=1,
        username=token + "decoded",
        hashed_password="root",
        created_at=datetime.now(),
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    user = decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@router.get("/register")
def get_register():
    return {"message": "Registration form."}


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: db_dependency):
    """
    Creates a new user with a hashed password and stores it in the database.
    """
    new_user = User(
        username=user.username,
        hashed_password=bcrypt_context.hash(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Created user account succesfully."}


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
    return


@router.get("/login")
def get_login():
    return {"message": "Login form."}


@router.post("/login")
def login_user():
    return {"message": "Authenticate user and start session."}


@router.get("/logout")
def logout():
    return {"message": "End session and redirect to homepage."}
