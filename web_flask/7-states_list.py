#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage, storage.all
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Removes the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted
    by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B> """
    states = sorted(storage.all('State').values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0')
