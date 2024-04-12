#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
with Fifth routes
"""

from flask import Flask, request, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html(n):
    """ display a HTML page only if n is an integer: 

    H1 tag: “Number: n” inside the tag BODY """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
