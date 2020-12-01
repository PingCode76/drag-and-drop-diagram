import math
from models import db, Label

def addLabelAPI(nb1,nb2):
    #db.create_all()
    Label1 = Label(var1=nb1,var2=nb2)
    db.session.add(Label1)
    db.session.commit()
    return {"labelStatus": "added in DB"}