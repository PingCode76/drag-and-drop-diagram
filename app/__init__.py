from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .views import app
from . import models

from app.models import db, Label

# Connect sqlalchemy to app
models.db.init_app(app)

