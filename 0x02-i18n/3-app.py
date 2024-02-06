#!/usr/bin/env python3
""" Flask App """


from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


babel.init_app(app, directory='translations')


@app.route('/')
def index():
    """ index page """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
