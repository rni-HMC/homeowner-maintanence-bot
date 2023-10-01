import os

from flask import Flask, render_template

from src.connect import connect_via_envvars
from src.tasks import get_tasks

app = Flask(__name__)


@app.route("/")
def get_countries():
    engine = connect_via_envvars(env_file_path=os.getenv("ENV_FILE_PATH"))
    tasks_to_display = get_tasks(engine)
    return render_template("home.html", tasks=tasks_to_display)
