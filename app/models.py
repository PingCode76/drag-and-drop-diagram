from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, jsonify
import datetime
import logging as lg

#from .views import app
# for install SQL postgres config
# use https://blog.theodo.com/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/ 

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    #def __init__(self, *args):
        #super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Label(db.Model):
    """Model for the Label table"""
    __tablename__ = 'Label'

    id = db.Column(db.Integer, primary_key = True)
    var1 = db.Column(db.Integer)
    var2 = db.Column(db.Integer)