# coding=utf8

import unittest
from flask import current_app
from app_blog import create_app, db
from app_blog.models import User

class IndexTestCast(unittest.TestCase):
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


    def test_select_from_users(self):
        users = User.query.all()
        print users
        self.assertIsNotNone(users)


