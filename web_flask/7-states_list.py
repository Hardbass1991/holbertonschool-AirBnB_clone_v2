#!/usr/bin/python3
"""Module that displays template with data from storage"""
from models import storage, storage_type
from models.state import State
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def number_template():
    """View that renders a template with all State instances"""
    states = list(storage.all(State).values())
    storage.close()

    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
