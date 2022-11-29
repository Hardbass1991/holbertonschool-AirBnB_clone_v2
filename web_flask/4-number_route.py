#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask, abort
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """View that shows a greeting"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """View that literally displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text=""):
    """View that displays 'C' followed by input string

    Keyword arguments:
    text - input text
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """View that display 'Python' followed by input text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def number_n(n):
    """View that displays 'n is a number' if n is integer"""
    if not n.isnumeric():
        abort(404)
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
