from flask import Flask, render_template, url_for, request, jsonify
from models import db
from .controllers.utils import *

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

POSTGRES = {
    'user': 'postgres',
    'pw': '000000',
    'db': 'bdddragdrop',
    'host': 'localhost',
    'port': '5432',
}
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)


@app.route('/')
def index():
    #indexCalcul()
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')
