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


@app.route("/c/<text>", strict_slashes=False)
def C_text(text=""):
    """View that displays 'C' followed by input string

    Keyword arguments:
    text - input text
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
