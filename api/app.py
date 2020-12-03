from flask import Flask
from flask_cors import CORS
from apiFunction import addLabelAPI, addRecordAPI, createDataAPI
from markupsafe import escape
import models
from models import db, Label, Record

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
models.db.init_app(app)

@app.route("/")
def home():
    return {"home": "Welcome to Flask API"}

# Route : /addLabel/{title}/{node1}/{node2}/{functionNumber}/{column}
@app.route("/addLabel/<string:title>/<string:node1>/<string:node2>/<int:functionNumber>/<int:column>", methods=['GET'])
def addLabel(title,node1,node2,functionNumber,column):
    # try this route: addLabel/loremIpsum/BR45/CV10/1/1
    return addLabelAPI(str(title), str(node1), str(node2), int(functionNumber), int(column))

# Route : /removeLabel/{id}
@app.route("/removeLabel/<int:id>")
def removeLabel(id):
    label = Label.query.get(id)
    db.session.delete(label)
    db.session.commit()
    return {"database": "label" + str(id) + "has been deleted"}

# Route : /label/{id}
@app.route("/label/<int:id>")
def labelInformation(id):
    label = Label.query.get(id)
    if(label):
        return {"id": str(id), "title": label.title}
    else:
        return {"database" : "Label"+ str(id) + " not exist"}
    
# Route : /labels
@app.route("/labels")
def listLabels():
    dict = {}
    labels = Label.query.all()
    for label in labels:
        dict.update({label.id : label.title})
    return dict

#TODO: update label ?
####################################


# Route : /addRecord/{title}/{labels} # enum ?
@app.route("/addRecord/<string:title>/<int:labels>", methods=['GET'])
def addRecord(title,labels):
    # try this route: addRecord/recordTestTitle/5
    return addRecordAPI(str(title),int(labels))
    
#list of records /records
@app.route("/records")
def listRecords():
    dict = {}
    records = Record.query.all()
    for record in records:
        dict.update({record.id : record.title})
    return dict

# Route : /record/{id}
@app.route("/record/<int:id>")
def recordInformation(id):
    record = Record.query.get(id)
    if(record):
        return {"id": str(id), "title": record.title}
    else:
        return {"database" : "Record "+ str(id) + " not exist"}

# Route : /removeRecord/{id}
@app.route("/removeRecord/<int:id>")
def removeRecord(id):
    record = Record.query.get(id)
    db.session.delete(record)
    db.session.commit()
    return {"database": "record " + str(id) + "has been deleted"}


#TODO: relation Record.labels -> label

# for create a testData
@app.route("/createData", methods=['GET'])
def createData():
    return createDataAPI()

