# import datetime

from sqlalchemy import Engine, text

from src.connect import connect_via_envvars


def keepalive(engine: Engine):
    with engine.connect() as con:
        # now = datetime.datetime.utcnow()  # TODO use datetime in the future
        con.execute(text("INSERT INTO keepalive VALUES (NULL)"))
        result = con.execute(text("SELECT * FROM keepalive"))
    return result


if __name__ == "__main__":
    engine = connect_via_envvars()
    result = keepalive(engine)
    print(result.fetchall())
