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
        """
        Will be called before every test
        """

        db.session.commit()
        db.drop_all()
        db.create_all()
        #deleting then creating all the apps so its fresh ready for testing.

        # create test admin user
        admin = Passwords( password="password")


        # create test non-admin user
        employee = Passwords(password="test" )

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()
        
        #drops all tables after every test


class TestApp(TestBase):
    
    #test to check that the homepage is accessible. code 200 means it has recieved a positive response
    def test_hompage(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


     #test to check that the about page is accessible. code 200 means it has recieved a positive response
    def  test_about(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)


    def test_getPrize_page_view(self):
        response = self.client.get(url_for("button0"))
        self.assertEqual(response.status_code, 200)

    def test_getPrize_page_view(self):
        response = self.client.get(url_for("button1"))
        self.assertEqual(response.status_code, 200)


    def test_getPrize_page_view(self):
        response = self.client.get(url_for("button2"))
        self.assertEqual(response.status_code, 200)



    def test_getPrize_page_view(self):
        response = self.client.get(url_for("button3"))
        self.assertEqual(response.status_code, 200)


