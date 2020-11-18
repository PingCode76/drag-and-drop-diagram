import math
from models import db, Label

def addLabelAPI():
    #db.create_all()
    Label1 = Label(var1=1,var2=2)
    db.session.add(Label1)
    db.session.commit()
    return {"labelStatus": "added"}