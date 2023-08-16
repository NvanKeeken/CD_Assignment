# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return "Welcome, to my final winc assignment: CD! I hope it will work, yes!"

@app.route('/requirements')
def requirements():
    return 'The requirments are: build a continuous deployment using Git Actions'

