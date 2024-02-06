#!/usr/bin/env python3
""" Falsk App """

from flask import Falsk, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
