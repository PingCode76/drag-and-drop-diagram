from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .views import app
#import models
from models import db

# Connect sqlalchemy to app
#models.db.init_app(app)

#@app.cli.command()
#def init_db():
    #models.init_db()


POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'bdd-drag-drop',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)
