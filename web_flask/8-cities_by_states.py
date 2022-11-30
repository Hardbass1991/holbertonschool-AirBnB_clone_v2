#!/usr/bin/python3
"""Module that displays template with data from storage"""
from models import storage, storage_type
from models.city import City
from models.state import State
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """View that renders a template with all City instances by State"""
    d = {}
    states = storage.all(State).values()
    for state in states:
        d[state.name] = {}
        d[state.name]["id"] = state.id
        if storage_type == "db":
            d[state.name]["cities"] = state.cities
        else:
            d[state.name]["cities"] = state.cities()

    storage.close()

    return render_template('8-cities_by_states.html', d=d)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
