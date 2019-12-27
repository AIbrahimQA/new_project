from flask import request
from application import app
import requests
import random
import string



@app.route("/getPassStrength", methods=["POST"])
def getPassStrength():
    password = request.json["password"]
    prizes = len(password)
    if prizes >= 10:
        return {"strength":"Strong Password"}
    else:
        return {"strength":"Weak Password"}
    return {"strength":"0"}
