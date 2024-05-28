#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


class Config(object):
    """ app configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """user login details or none"""
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """ find user if any and set it to global"""
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/')
def index() -> str:
    """ render html file"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
