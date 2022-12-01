#!/usr/bin/python3
"""Module that displays lists of cities by state, and list of amenities"""
from models import storage, storage_type
from models.amenity import Amenity
from models.city import City
from models.state import State
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """View that renders popover lists of cities and amenities"""
    d = {}
    states = list(storage.all(State).values())
    for state in states:
        d[state.name] = {}
        d[state.name]["id"] = state.id
        if storage_type == "db":
            d[state.name]["cities"] = state.cities
        else:
            d[state.name]["cities"] = state.cities()
    
    amenities = list(storage.all(Amenity).values())
    storage.close()

    return render_template("10-hbnb_filters.html", d=d, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
