from flask import request, render_template, session
from application import app, db
from application.models import Passwords 
import requests
import os

buttons = ["Generate Password", "Password Strength"]

@app.route("/")
def home():
        return render_template("home.html", buttons=buttons )

@app.route("/getPassword", methods=["GET"])
def button0():
    res = requests.post( "http://service4:5000/getPassword" )
    if res.ok:
        session["password"] = res.json()["password"]
        pass1 = Passwords(password=session.get("password"))
        db.session.add(pass1)
        db.session.commit()
    



        return render_template("home.html", buttons=buttons, password=session.get("password"))
    return "request failed"

@app.route("/getPassStrength", methods=["GET"])
def button1():
    res = requests.post( "http://service5:5000/getPassStrength", json={"password":session.get("password")} )
    if res.ok:
        return render_template("home.html", buttons=buttons, password=session.get("password"), strength="This password is a "+res.json()["strength"] )

    return "request failed"
