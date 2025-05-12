from datetime import datetime
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

from db.schema import UserResponse

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# TODO: User Authentication - Store user sessions using signed cookies or dependency injection


def decode_token(token):
    return UserResponse(
        id=1,
        username=token + "decoded",
        hashed_password="root",
        created_at=datetime.now(),
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = decode_token(token)
    return user


@router.get("/users/me")
async def read_users_me(current_user: Annotated[UserResponse, Depends(oauth2_scheme)]):
    return current_user


@router.get("/authtest")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


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
