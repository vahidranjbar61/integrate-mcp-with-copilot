from typing import Optional
from sqlmodel import SQLModel, Field


class Participant(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    activity_id: int = Field(foreign_key="activity.id")
    student_email: str


class Activity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    description: Optional[str] = None
    schedule: Optional[str] = None
    max_participants: Optional[int] = None


class Student(SQLModel, table=True):
    admission_no: str = Field(primary_key=True, index=True)
    name: str
    email: Optional[str] = None
    grade: Optional[str] = None
    photo_path: Optional[str] = None
