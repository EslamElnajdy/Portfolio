#!/usr/bin/python3
""" the entry point to the app """

from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__, static_url_path='/static')


year = datetime.now().year


@app.route('/')
def about():

    return render_template('about.html', year=year)


@app.route('/projects')
def projects():
    return render_template('projects.html', year=year)


if __name__ == '__main__':
    app.run(debug=True)
