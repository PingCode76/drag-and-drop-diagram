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
#from .models import Label
from app.models import db, Label

def indexCalcul():
    #db.create_all()
    Label1 = Label(var1=20,var2=50)
    db.session.add(Label1)
    db.session.commit()