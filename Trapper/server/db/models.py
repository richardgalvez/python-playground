from sqlalchemy import create_engine, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from datetime import datetime

url = URL.create(
    drivername="postgresql",
    username="tadmin",
    password="troot",
    host="postgres",
    database="trapper-db",
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


class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    priority = Column(String)
    status = Column(String, default="open")
    # user_id: foreign key to User
    created_at = Column(DateTime, default=datetime.now)
