from flask import Flask
from flask_cors import CORS
from apiFunction import addLabelAPI
import models

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
models.db.init_app(app)

@app.route("/greeting")
def greeting():
    return {"greeting": "Hello from Flask!"}

@app.route("/addLabel")
def addLabel():
    return addLabelAPI()


#def indexCalcul(): 
    #db.create_all()
    #Label1 = Label(var1=20,var2=50)
    #db.session.add(Label1)
    #db.session.commit() 


