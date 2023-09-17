import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine, text


def connect_via_envvars() -> Engine:
    # Load environment variables from the .env file
    load_dotenv(dotenv_path=Path(__file__).parent.parent.parent / ".env")

    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE = os.getenv("DATABASE")

    connection_string = (
        "mysql+mysqlconnector://"
        f"{DATABASE_USERNAME}:{DATABASE_PASSWORD}"
        f"@{DATABASE_HOST}:3306/{DATABASE}"
    )

    engine = create_engine(connection_string, echo=True)
    return engine


def delete_table_by_name(engine: Engine, table_name: str):
    with engine.connect() as connection:
        connection.execute(text(f"DROP TABLE IF EXISTS {table_name}"))


def delete_all_tables(engine: Engine):
    delete_table_by_name(engine, "example")


def execute_sql_file(engine: Engine, filepath: Path):
    with engine.connect() as con:
        with open(filepath.resolve()) as file:
            queries = file.read().split(";\n\n")
            for query in queries:
                con.execute(text(query))


def initialize_db(engine: Engine):
    execute_sql_file(
        engine,
        Path(__file__).parent / "0001_init_schema.up.sql",
    )


def delete_db(engine: Engine):
    execute_sql_file(
        engine,
        Path(__file__).parent / "0001_init_schema.down.sql",
    )


if __name__ == "__main__":
    engine = connect_via_envvars()
    initialize_db(engine)
    # delete_db(engine)
