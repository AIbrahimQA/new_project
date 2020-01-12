
from flask import request
from application import app
import requests
import random
import string

@app.route("/getLetter", methods=["POST"])
def getLetter():
#    return {"letter":random.choice(string.ascii_uppercase)}
    return {"letter":random.choice(string.ascii_lowercase)}

