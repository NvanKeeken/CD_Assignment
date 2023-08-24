from flask import Flask, render_template, redirect, url_for

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


# # 
# # Import what we need from flask
# from flask import Flask

# # Create a Flask app inside `app`
# app = Flask(__name__)

# # Assign a function to be called when the path `/` is requested
# @app.route('/')
# def index():
#     return "Welcome, to my final winc assignment: CD! I hope it will work!"

# @app.route('/requirements')
# def requirements():
#     return 'The requirments are: build a continuous deployment using Git Actions'

