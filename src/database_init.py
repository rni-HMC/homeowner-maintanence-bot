import os

from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine, text


def connect_via_envvars() -> Engine:
    # Load environment variables from the .env file
    load_dotenv()

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


def create_example_table(engine: Engine):
    with engine.connect() as connection:
        connection.execute(
            text("CREATE TABLE example " "(id INTEGER, name VARCHAR(20))")
        )
        connection.execute(
            text("INSERT INTO example (name) VALUES (:name)"),
            {"name": "Ashley"},
        )
        connection.execute(
            text("INSERT INTO example (name) VALUES (:name)"),
            [{"name": "Barry"}, {"name": "Christina"}],
        )
        connection.commit()

        result = connection.execute(
            text("SELECT * FROM example WHERE name = :name"),
            dict(name="Ashley"),
        )

        for row in result.mappings():
            print("Author:", row["name"])


def delete_table_by_name(engine: Engine, table_name: str):
    with engine.connect() as connection:
        connection.execute(text(f"DROP TABLE IF EXISTS {table_name}"))


def delete_all_tables(engine: Engine):
    delete_table_by_name(engine, "example")


if __name__ == "__main__":
    engine = connect_via_envvars()
    create_example_table(engine)
    delete_table_by_name(engine, "example")
