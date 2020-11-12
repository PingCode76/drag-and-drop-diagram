import random
import os.path
import os
import shutil
import xlrd
import svgwrite
import logging as lg

from random import randint
from models import db

#print("util.py executed")
def indexCalcul():
    db.session.add(table1(2.50,250,1))
    db.session.commit()