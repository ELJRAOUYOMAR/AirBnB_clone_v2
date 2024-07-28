#!/usr/bin/python3
""" module doc """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ def doc """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ def doc """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ C is fun """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text):
    """ Python is fun """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ def doc """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>/', strict_slashes=False)
def first_render(n):
    """ render a template"""
    return render_template("5-number.html", number_n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)