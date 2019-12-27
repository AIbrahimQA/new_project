from flask import request, render_template, session
from application import app
import requests
import os

buttons = ["Generate Password"]

@app.route("/")
def home():
        return render_template("home.html", buttons=buttons )

@app.route("/getPassword", methods=["GET"])
def button0():
    res = requests.post( "http://service4:5000/getPassword" )
    if res.ok:
        session["password"] = res.json()["password"]
        return render_template("home.html", title=title, buttons=buttons, password=session.get("password"))
    return "request failed"

