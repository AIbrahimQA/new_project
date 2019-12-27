
from flask import Flask
app = Flask(__name__)
app.secret_key = 'some secret key'
from application import routes
