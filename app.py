from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    #   names = ["David", "Fred", "Bruce", "Sally"]
    return render_template("about.html")
