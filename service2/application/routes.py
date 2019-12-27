
from flask import request, render_template
from application import app
import requests
import random
import string 

@app.route("/getDigits", methods=["POST"])
def getDigits():
    return {"digits":string.digits}

