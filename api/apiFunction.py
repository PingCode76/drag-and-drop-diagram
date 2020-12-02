import math
from models import db, Label

#return addLabelAPI(escape(title),escape(node1),escape(node2),escape(functionNumber), escape(column))
def addLabelAPI(title,node1,node2,functionNumber,column):
    #db.create_all()
    Label1 = Label(title=title, node1=node1, node2=node2, functionNumber=functionNumber, column=column)
    db.session.add(Label1)
    db.session.commit()
    return {"labelStatus": "added in database"}