import datetime
import os
from typing import List

from sqlalchemy import DateTime, Engine, String, Text, select
from sqlalchemy.sql import func

from src.connect import connect_via_envvars

from sqlalchemy.orm import (  # isort:skip
    DeclarativeBase,  # isort:skip
    Mapped,  # isort:skip
    Session,  # isort:skip
    mapped_column,  # isort:skip
    relationship,  # isort:skip
)


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    seconds_between_completions: Mapped[int]
    cost: Mapped[int]
    task_type_id: Mapped[int]
    task_type: Mapped["TaskType"] = relationship(
        primaryjoin="foreign(TaskType.id) == Task.task_type_id",
    )
    area_id: Mapped[int]
    area: Mapped["Area"] = relationship(
        primaryjoin="foreign(Area.id) == Task.area_id",
    )
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class TaskType(Base):
    __tablename__ = "task_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)


class Area(Base):
    __tablename__ = "areas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    attempts: Mapped[List["Attempt"]] = relationship(
        primaryjoin="foreign(Attempt.user_id) == User.id"
    )


class Attempt(Base):
    __tablename__ = "attempts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
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


class KeepAlive(Base):
    __tablename__ = "keepalive"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    kept_alive_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


def populate_data(engine: Engine):
    with Session(engine) as session:
        kitchen = Area(name="Kitchen", description="Kitchen tasks")
        inspection = TaskType(
            name="Inspection",
            description="Inspection tasks",
        )
        richard = User(name="Richard")
        session.add_all([kitchen, inspection, richard])
        session.commit()

        inspect_kitchen_sink = Task(
            name="Inspect Kitchen Sink",
            description="Inspect the kitchen sink",
            seconds_between_completions=86400,
            cost=0,
            task_type_id=inspection.id,
            area_id=kitchen.id,
        )
        session.add_all([kitchen, inspection, inspect_kitchen_sink])
        session.commit()

        attempt_1 = Attempt(
            user_id=richard.id,
            task_id=inspect_kitchen_sink.id,
            title="Kitchen Sink Inspection Attempt 1",
            notes=(
                "I forgot to put on my glasses,"
                " couldn't inspect anything b/c too blurry"
            ),
            status="Failed",
            cost=0,
        )

        attempt_2 = Attempt(
            user_id=richard.id,
            task_id=inspect_kitchen_sink.id,
            title="Kitchen Sink Inspection Attempt 1",
            notes="The kitchen sink is clean",
            status="Completed",
            cost=0,
        )

        session.add_all([attempt_1, attempt_2])
        session.commit()

        initial_keepalive_heartbeat = KeepAlive()
        session.add_all([initial_keepalive_heartbeat])
        session.commit()


def validate_data(engine: Engine):
    print("VALIDATING DATA ***************")
    with Session(engine) as session:
        session.execute(select(Area).where(Area.name == "Kitchen"))
        print("RESULT ABOVE ^^^^")
        session.execute(select(TaskType).where(TaskType.name == "Inspection"))
        print("RESULT ABOVE ^^^^")
        session.execute(select(Task))
        print("RESULT ABOVE ^^^^")
        session.execute(select(Attempt))
        print("RESULT ABOVE ^^^^")
        result = session.execute(select(User).where(User.name == "Richard"))
        print("RESULT ABOVE ^^^^")
        richard: User = result.all()[0][0]
        # TODO idk why accessing this is so weird
        print(f"Richard.id: {richard.id}")
        print(f"Richard.name: {richard.name}")
        print(f"Richard.created_date: {richard.created_date}")
        print(f"Richard.attempts: {richard.attempts}")
        print("RESULT ABOVE ^^^^")
        session.execute(select(KeepAlive))
        print("RESULT ABOVE ^^^^")


def initialize_db():
    engine = connect_via_envvars(env_file_path=os.getenv("ENV_FILE_PATH"))
    Base.metadata.create_all(engine)
    populate_data(engine)
    validate_data(engine)


def delete_db():
    engine = connect_via_envvars(env_file_path=os.getenv("ENV_FILE_PATH"))
    Base.metadata.drop_all(engine)


if __name__ == "__main__":
    delete_db()
    initialize_db()
