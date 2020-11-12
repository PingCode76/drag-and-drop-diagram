import random
import os.path
import os
import shutil
import xlrd
import svgwrite
import logging as lg

from random import randint
from models import *

#print("util.py executed")
def indexCalcul():
    #db.create_all()
    
    db.session.add(Table(250,240))
    db.session.commit()