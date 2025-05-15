from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
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


@router.get("/register")
def get_register():
    return {"message": "Registration form."}


@router.post("/register", status_code=status.HTTP_201_CREATED)
# TODO: Refactor to use the UserCreate class?
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
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency):
    """
    Decodes the JWT token and retrieves user details.
    Raises an exception if the token is invalid (details incorrect) or expired.
    """
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
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    """
    Authenticates user credentials and returns a JWT token if valid.
    """
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not authenticated."
        )
    username = str(user.username)
    user_id = user.id
    token = create_access_token(username, user_id, timedelta(minutes=30))

    return {"access_token": token, "token_type": "bearer"}


user_dependency = Annotated[dict, Depends(get_current_user)]


# Authentication via dependency injection is working.
@router.get("/auth", status_code=status.HTTP_200_OK)
async def check_auth(user: user_dependency):
    return {"User": user}


@router.post("/login")
async def login_user():
    return {"message": "Authenticate user and start session."}


@router.get("/logout")
async def logout():
    return {"message": "End session and redirect to homepage."}
