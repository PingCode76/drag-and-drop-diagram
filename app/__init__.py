from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .views import app
from . import models
#import models
#from models import db
#import models


# Connect sqlalchemy to app
models.db.init_app(app)
db = SQLAlchemy(app)

#models.init_db()
#@app.cli.command()
#def init_db():
    #models.init_db()
