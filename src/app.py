from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_countries():
    return render_template("home.html")
