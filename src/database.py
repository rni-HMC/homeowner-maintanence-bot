import datetime
import os

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func

from src.connect import connect_via_envvars


class Base(DeclarativeBase):
    pass


# an example mapping using the base
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    seconds_between_completions: Mapped[int]
    cost: Mapped[int]
    type_id: Mapped[int]
    area_id: Mapped[int]
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class TaskType(Base):
    __tablename__ = "task_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)


class Area(Base):
    __tablename__ = "areas"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class Attempt(Base):
    __tablename__ = "attempts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    task_id: Mapped[int]
    title: Mapped[str] = mapped_column(String(255))
    notes: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(255))
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    completed_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    cost: Mapped[int]


def initialize_db():
    engine = connect_via_envvars(env_file_path=os.getenv("ENV_FILE_PATH"))
    Base.metadata.create_all(engine)


def delete_db():
    engine = connect_via_envvars(env_file_path=os.getenv("ENV_FILE_PATH"))
    Base.metadata.drop_all(engine)


if __name__ == "__main__":
    # initialize_db()
    delete_db()
