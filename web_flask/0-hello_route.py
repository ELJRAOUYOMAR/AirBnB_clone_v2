#!/usr/bin/python3
""" module doc """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ def doc """
    return "Hello HBNB!"