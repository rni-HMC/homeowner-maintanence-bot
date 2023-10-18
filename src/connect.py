import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine


def connect_via_envvars(
    env_file_path: Path = Path(__file__).parent.parent.parent / ".env",
) -> Engine:
    # Load environment variables from the .env file
    load_dotenv(dotenv_path=env_file_path)

    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE = os.getenv("DATABASE")

    connection_string = (
        "mysql+mysqlconnector://" f"{DATABASE_USERNAME}:{DATABASE_PASSWORD}" f"@{DATABASE_HOST}:3306/{DATABASE}"
    )

    engine = create_engine(connection_string, echo=True)
    return engine
