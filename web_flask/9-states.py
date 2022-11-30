#!/usr/bin/python3
"""Module that displays two views showing a list of states and a list of cities by state"""
from models import storage, storage_type
from models.city import City
from models.state import State
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """View that renders a template with all State instances"""
    states = list(storage.all(State).values())
    storage.close()

    return render_template("9-states.html", states=states, state_id=None)


@app.route("/states/<id>", strict_slashes=False)
def cities_by_states(id):
    """View that renders a template with all City instances by State"""
    d = {}
    states = storage.all(State).values()
    states = [x for x in states if x.id == id]

    if not states:
        storage.close()
        return render_template("9-states.html", d=d, state_id=id)  

    for state in states:
        d[state.name] = {}
        d[state.name]["id"] = state.id
        if storage_type == "db":
            d[state.name]["cities"] = state.cities
        else:
            d[state.name]["cities"] = state.cities()

    storage.close()

    return render_template("9-states.html", d=d, state_id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
