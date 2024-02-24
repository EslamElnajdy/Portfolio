#!/usr/bin/python3
""" the entry point to the app """

from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__, static_url_path='/static')


year = datetime.now().year


@app.route('/')
def about():

    return render_template('about.html', year=year, title="About")


@app.route('/projects')
def projects():
    return render_template('projects.html', year=year, title="Projects")


@app.route('/skills')
def skills():
    return render_template('skills.html', year=year, title="Skills")


@app.route('/education')
def education():
    return render_template('education.html', year=year, title="Education")


@app.route('/achievements')
def achievements():
    return render_template('achievements.html', year=year, title="Achievements")


@app.route('/volunteer-Work')
def Volunteer_Work():
    return render_template('volunteer_work.html', year=year, title="Volunteer Work")


@app.route('/blog')
def blog():
    return render_template('blog.html', year=year, title="Blog")

if __name__ == '__main__':
    app.run(debug=False)
