from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

@app.route("/greeting")
def greeting():
    return {"greeting": "Hello from Flask!"}


#def indexCalcul(): 
    #db.create_all()
    #Label1 = Label(var1=20,var2=50)
    #db.session.add(Label1)
    #db.session.commit() 


