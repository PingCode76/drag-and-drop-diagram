from flask import Flask
from flask_cors import CORS
from apiFunction import addLabelAPI
from markupsafe import escape
import models
from models import db, Label

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
models.db.init_app(app)

@app.route("/")
def home():
    return {"home": "it's Home page"}

@app.route("/greeting")
def greeting():
    return {"greeting": "Hello from Flask API"}

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
