#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request


app = Flask(__name__, template_folder="templates")


@app.route('/')
def index() -> str:
    """ render html """
    return render_template("index.html")


if __name__ == "__main__":
    app.run
