from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#test commmit

from db import query 

@app.route("/dbu")
def dbu():
    return query("Select * from team10.events")

# app.route("/addEvent")
# def addEvent():

