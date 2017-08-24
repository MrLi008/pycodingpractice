# coding=utf8
from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from wtforms.validators import DataRequired
import unittest

from app_blog.managedb.constructionflaskform import ConstructionFlaskForm


class WtfFormTestCase(unittest.TestCase):

    def test_init(self):
        params = {
            'name': {
                'type': 'StringField',
                'name': '123456',
                'validators': [DataRequired()]
            }
        }
        cf = ConstructionFlaskForm(params=params)
        print cf
        # print cf.MyFlaskForm.__dict__
        newform = cf.convertdicttowtfform()
        print cf
        print newform.__dict__
        # print cf.MyFlaskForm.__dict__
        self.assertTrue(True)

    def test_init2(self):
        params = {
            'name': {
                'type': 'StringField',
                'name': '123456',
                'validators': [DataRequired()]
            },
            'value': {
                'type': 'StringField',
                'name': '1234568',
                'validators': [DataRequired()]
            }
        }
        cf = ConstructionFlaskForm(params=params)
        print cf
        # print cf.MyFlaskForm.__dict__
        newform = cf.convertdicttowtfform()
        print cf
        print newform.__dict__
        # print cf.MyFlaskForm.__dict__
        self.assertTrue(True)