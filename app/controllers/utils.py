import random
import os.path
import os
import shutil
import xlrd
import svgwrite
import logging as lg

from flask_sqlalchemy import SQLAlchemy
from random import randint
from models import Label
#from views import db

db = SQLAlchemy()

#print("util.py executed")
def indexCalcul():
    #db.create_all()
    Label1 = Label(var1=20,var2=50)
    db.session.add(Label1)
    db.session.commit()