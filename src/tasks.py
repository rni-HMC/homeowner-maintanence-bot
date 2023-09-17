from sqlalchemy import Engine, text

from src.connect import connect_via_envvars


def get_tasks(engine: Engine):
    with engine.connect() as con:
        result = con.execute(text("SELECT * FROM tasks"))
        tasks = [dict(row) for row in result.mappings()]
        return tasks


if __name__ == "__main__":
    engine = connect_via_envvars()
    tasks = get_tasks(engine)
    print(f"tasks: {tasks}")
    print(f"type: {type(tasks)}")
    print(f"type(tasks[0]): {type(tasks[0])}")
