#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
with Routes
"""

from flask import Flask, render_template

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
    new = text.replace('_', ' ')
    return 'C %s' % new


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ display “Python ”, followed by the value of the <text> 

    replace underscore _ symbols with a space """
    new = text.replace('_', ' ')
    return 'Python %s' % new


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer """
    if type(n) == int:
        return '%i is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display a HTML page only if n is an integer: 

    H1 tag: “Number: n” inside the tag BODY """
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ display a HTML page only if n is an integer: 

    H1 tag: “Number: n is even|odd” inside the tag BODY """
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0')
