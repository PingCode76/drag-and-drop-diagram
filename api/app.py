from flask import Flask
from flask_cors import CORS
from apiFunction import addLabelAPI
from markupsafe import escape
import models

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

@app.route("/addLabel/<nb1>/<nb2>")
def addLabel(nb1,nb2):
    return addLabelAPI(escape(nb1),escape(nb2))
    

