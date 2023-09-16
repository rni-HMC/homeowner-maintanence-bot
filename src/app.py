from flask import Flask, render_template

app = Flask(__name__)

TASKS = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Go to the store and buy groceries.",
        "done": False,
        "due_date": "2023-12-31",
        "frequency": "daily",
    },
    {
        "id": 2,
        "title": "Wash car",
        "description": "Wash the car and clean the interior.",
        "done": False,
        "due_date": "2023-11-05",
        "frequency": "weekly",
    },
]


@app.route("/")
def get_countries():
    return render_template("home.html", tasks=TASKS)
