from flask import Flask, render_template

app = Flask(__name__)

TASKS = [
    {
        "id": 1,
        "title": "Exercise Angle Stops",
        "description": "Turn the knob on and off a few times."
        " Don't try to force it to turn — doing so could cause the"
        " valve to break.",
        "done": False,
        "due_date": "2023-12-31",
        "frequency": "daily",
    },
    {
        "id": 2,
        "title": "Replace Angle Stops",
        "description": "Shut off water mainlines. Replace.",
        "done": False,
        "due_date": "2023-11-05",
        "frequency": "weekly",
    },
    {
        "id": 3,
        "title": "Replace Shower Cartridge",
        "description": "Shut off water mainlines. Replace.",
        "done": False,
        "due_date": "2023-11-25",
        "frequency": "weekly",
    },
]


@app.route("/")
def get_countries():
    return render_template("home.html", tasks=TASKS)
