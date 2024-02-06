#!/usr/bin/env python3
""" Flask app """


from flask import Flask, request
from flask_babel import Babel


class config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

def get_locale():
    """ Determine the best match with the supported languages """
    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
