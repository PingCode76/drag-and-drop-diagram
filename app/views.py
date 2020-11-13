from flask import Flask, render_template, url_for, request, jsonify
#from .models import db
from .utils import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def index():
    indexCalcul()
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')
