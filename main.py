from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route("/home", methods=["GET"])
def home():
    return redirect(url_for("index"), 302)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", title="Index")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About")



