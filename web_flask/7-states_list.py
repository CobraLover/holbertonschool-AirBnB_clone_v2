#!/usr/bin/python3
"""Starts a Flask web application"""

from models import storage
from models.state import State
from flask import Flask, render_template
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Returns a rendered html template 
    at the /states_list route, listing all states """
    states = sorted(storage.all('State').values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """ Removes the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0')
