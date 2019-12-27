from flask import request
from application import app
import requests
import random
from random import randint
from random import choice
import string
import os



@app.route("/getPassword", methods=["POST"])
def getPassword():
    password = ""
    randomDigit = requests.post( "http://service2:5000/getDigits" )
    randomLetter = requests.post( "http://service3:5000/getLetter" )

    characters = str(randomDigit) + str(randomLetter)
    password = "".join(choice(characters) for x in range(randint(8, 16))) 

    return {"password":password}

