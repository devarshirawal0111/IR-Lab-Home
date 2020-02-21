from app import app
from flask import render_template, request
import json

from app.helpers import *

@app.route('/index')
@app.route('/')
def index():
    images = getCarouselImageURL(n=4)
    return render_template('index.html', images = images , _show_ = 0)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/publications')
def publications():
    with open('./app/static/Data/publications.json', 'r') as file:
        data = json.loads(file.read())
    print(data)
    return render_template('publications.html', data = data)

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')
