from pathlib import Path

from sqlalchemy import Engine, text

from src.connect import connect_via_envvars


def execute_sql_file(engine: Engine, filepath: Path):
    with engine.connect() as con:
        with open(filepath.resolve()) as file:
            queries = file.read().split(";\n\n")
            for query in queries:
                con.execute(text(query))
        con.commit()


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


def add_data(engine: Engine):
    execute_sql_file(
        engine,
        Path(__file__).parent / "0002_add_data.up.sql",
    )


if __name__ == "__main__":
    engine = connect_via_envvars()
    initialize_db(engine)
    add_data(engine)
    # delete_db(engine)
