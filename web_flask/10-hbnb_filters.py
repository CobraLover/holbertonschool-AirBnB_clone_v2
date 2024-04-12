#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """ /states: display a HTML page: (inside the tag BODY) 
    H1 tag: “States” 
    UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip 
    LI tag: description of one State: <state.id>: <B><state.name></B> 
    /states/<id>: display a HTML page: (inside the tag BODY) 
    If a State object is found with this id: 
    H1 tag: “State: ” 
    H3 tag: “Cities:” 
    UL tag: with the list of City objects linked to the State sorted by name (A->Z) 
    LI tag: description of one City: <city.id>: <B><city.name></B> 
    Otherwise: H1 tag: “Not found!” """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', **locals())


@app.teardown_appcontext
def teardown(self):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0')
