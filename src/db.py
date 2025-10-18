from sqlmodel import SQLModel, create_engine, Session
import os
from pathlib import Path

DB_PATH = os.environ.get("DATABASE_URL") or f"sqlite:///{Path(__file__).parent / 'data.db'}"
engine = create_engine(DB_PATH, echo=False)


def init_db():
    from .models import Activity, Student, Participant

    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
