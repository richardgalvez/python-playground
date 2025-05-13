from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, create_engine, Column, DateTime, Integer, String
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.engine import URL
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

DB_DRIVER = os.getenv("DB_DRIVER", "")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

url = URL.create(
    DB_DRIVER,
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME,
    port=5432,
)

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    priority = Column(String)
    status = Column(String, default="open")
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.now)
