from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .views import app
#import models
from models import db
import models
# Connect sqlalchemy to app
models.db.init_app(app)


#models.init_db()
#@app.cli.command()
#def init_db():
    #models.init_db()
