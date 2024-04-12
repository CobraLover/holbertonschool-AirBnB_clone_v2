#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
With four Routes
"""

from flask import Flask, escape, request

app = Flask(__name__)



@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def txt(text):
    """ display C and text """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ display C and text """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
