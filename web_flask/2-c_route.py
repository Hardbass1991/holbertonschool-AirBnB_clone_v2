#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """View that shows a greeting"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """View that literally displays 'HBNB'"""
    return "HBNB"


@app.route("/hbnb", strict_slashes=False)
def C_text(text=""):
    """View that displays 'C' followed by input string"""
    return f"C {text.replace("_", " ")}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
