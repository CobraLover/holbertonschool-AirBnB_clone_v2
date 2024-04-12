#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
With four Routes
"""

from flask import Flask, request

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
def c_text(text):
    """ display “C ”, followed by the value of the <text> 

    replace underscore _ symbols with a space """
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ display “Python ”, followed by the value of the <text> 

    replace underscore _ symbols with a space """
    formatted_text = text.replace('_', ' ')
    return "Python {}".format(formatted_text)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
