import random
import os.path
import os
import shutil
import xlrd
import svgwrite
import logging as lg

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, jsonify
from random import randint
from .models import Label
#from views import db

#app = Flask(__name__)
#app.config.from_object('config')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

#print("util.py executed")
def indexCalcul():
    #db.create_all()
    Label1 = Label(var1=20,var2=50)
    db.session.add(Label1)
    db.session.commit()