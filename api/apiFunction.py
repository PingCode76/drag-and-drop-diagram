import math
from models import db, Label, Record

#return addLabelAPI(escape(title),escape(node1),escape(node2),escape(functionNumber), escape(column))
def addLabelAPI(title,node1,node2,functionNumber,column):
    #db.create_all()
    Label1 = Label(title=title, node1=node1, node2=node2, functionNumber=functionNumber, column=column)
    db.session.add(Label1)
    db.session.commit()
    return {"labelStatus": "added in database"}

def addRecordAPI(title,labels):
    Record1 = Record(title=title,labels=labels)
    db.session.add(Record1)
    db.session.commit()
    return {"Record": "added in database"}

def createDataAPI():
    Record1 = Record(title='title1',labels=1)
    Record2 = Record(title='title2',labels=2)
    Record3 = Record(title='title3',labels=3)
    db.session.add(Record1)
    db.session.add(Record2)
    db.session.add(Record3)

    Label1 =  Label(title='title1',node1='BRTT',node2='BT87',functionNumber=1,column=2)
    Label2 =  Label(title='title2',node1='BRFC',node2='BT33',functionNumber=2,column=1)
    Label3 =  Label(title='title3',node1='BR34',node2='B584',functionNumber=2,column=1)
    db.session.add(Label1)
    db.session.add(Label2)
    db.session.add(Label3)
    db.session.commit()

    return {"database": "Successful, Data is created"}
