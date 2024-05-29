#!/usr/bin/env python3

"""
Basic Flask app with Babel extension

This module contains a Flask application that uses the Babel extension
for internationalization and localization.

The application has a single route '/' that renders the 'index.html' template.
The locale for the template is determined by the 'get_locale' function,
which selects the best match from the accepted languages in the request.

The application configuration is defined in the 'Config' class, which sets
the supported languages, default locale, and default timezone.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Configuration class for the Flask app

    Attributes:
        LANGUAGES (list): A list of supported language codes.
        BABEL_DEFAULT_LOCALE (str): The default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): The default timezone for the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines the locale for the current request.

    Returns:
        str: The best matching locale from the accepted languages in the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Renders the index.html template

    Returns:
        str: The rendered index.html template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
