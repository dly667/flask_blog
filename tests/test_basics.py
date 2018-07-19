import unittest
from flask import current_app,request
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_request_exists(self):
        with self.app.test_request_context(
        '/make_report/2017?format=1', data={'format': 'short'}):
            self.assertTrue(request.args.get('format') == '1')
        

