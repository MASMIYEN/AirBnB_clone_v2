#!/usr/bin/python3
""" This module defines a simple Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ This function is mapped to the root URL ("/")
    and returns the string "Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ This function is mapped to the URL "/hbnb" and returns the string "HBNB" """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ This function is mapped to the URL "/c/<text>"
    and returns the string 'c <text>',
    where <text> is a variable part of the URL. """
    return 'c {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ This function is mapped to the URL "/python/<text>"
    and returns the string 'Python <text>',
    where <text> is a variable part of the URL.
    If <text> is not provided, it defaults to 'is cool'. """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ This function is mapped to the URL "/number/<n>"
    and returns the string '<n> is a number',
    where <n> is a variable part of the URL
    and must be an integer. """
    return '{} is a number'.format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """This function is mapped to the URL "/number_odd_or_even/<n>"
    and returns a rendered HTML template,
    where <n> is a variable part of the URL
    and must be an integer.
    The template displays whether <n> is odd or even"""
    if n % 2 == 0:
        p = 'even'
    else:
        p = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, parity=p)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ This function is mapped to the URL "/states_list"
    and returns a rendered HTML template.
    The template displays a list of states retrieved from the storage"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """ This function is called after each request.
    It closes the storage to ensure
    that the session is properly removed
    and all resources are freed. """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ This function is mapped to the URL "/cities_by_states"
    and returns a rendered HTML template.
    The template displays a list of states
    and their cities retrieved from the storage. """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ Route function for /states and /states/<id> """
    not_found = False
    if id is not None:
        states = storage.all(State, id)
        with_id = True
        if len(states) == 0:
            not_found = True
    else:
        states = storage.all(State)
        with_id = False
    return render_template('9-states.html', states=states,
                           with_id=with_id, not_found=not_found)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
