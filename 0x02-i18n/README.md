# 0x02-i18n

This directory contains an introduction to the Flask-Babel extension for internationalization (i18n) and localization (l10n) in Flask applications, as well as the pytz library for handling time zones.

## Flask-Babel

Flask-Babel is an extension for Flask that provides internationalization and localization support. It allows you to translate text strings, format dates and times, and handle pluralization based on the user's locale.

### Installation

To install Flask-Babel, you can use pip:

pip install Flask-Babel

### Usage

1. Initialize Flask-Babel in your Flask application:

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(**name**)
babel = Babel(app)

2. Configure the available languages and the default language:

app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

3. Use the `gettext` function to mark strings for translation:

from flask_babel import gettext

@app.route('/')
def index():
message = gettext('Hello, World!')
return render_template('index.html', message=message)

4. Create translation files using the `pybabel` command-line tool:

pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l fr

5. Update the translation files with new strings:

pybabel update -i messages.pot -d translations

6. Translate the strings in the translation files.

7. Compile the translation files:

pybabel compile -d translations

## pytz

pytz is a library for handling time zones in Python. It provides a database of time zones and allows you to work with aware datetime objects, which include time zone information.

### Installation

To install pytz, you can use pip:

pip install pytz

### Usage

1. Import the pytz module:

import pytz

2. Get a time zone object:

tz = pytz.timezone('Europe/Paris')

3. Create an aware datetime object:

from datetime import datetime

now = datetime.now(tz)

4. Convert between time zones:

utc_now = now.astimezone(pytz.utc)

For more information and examples, refer to the Flask-Babel and pytz documentation.
