import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Passwords


class TestBase(TestCase):
    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':'+str(getenv('MYSQL_PASSWORD'))+'@'+str(getenv('MYSQL_HOST'))+'/'+str(getenv('MYSQL_DB_TEST')))       
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass

class TestApp(TestBase):
    
    #test to check that the homepage is accessible. code 200 means it has recieved a positive response
    def test_hompage(self):
        response = self.client.get(url_for('getPassword'))
        self.assertEqual(response.status_code, 200)
