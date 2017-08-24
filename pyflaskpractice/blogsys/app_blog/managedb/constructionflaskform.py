# coding=utf8
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired
import unittest


class ConstructionFlaskForm():


    '''
    :param kwargs 以name为k, 值包含: '类型', '名称', validators的数列


    '''

    def __init__(self, **kwargs):
        self.form = {}
        # check attribute is right
        for k, v in kwargs['params'].items():
            self.form[k] = {}
            self.form[k]['type'] = v.get('type')
            self.form[k]['name'] = v.get('name')
            self.form[k]['validators'] = v.get('validators')

        print self.form


    def convertdicttowtfform(self):
        class MyFlaskForm(FlaskForm):
            def __init__(self):
                super(MyFlaskForm, self).__init__()
        for k, v in self.form.items():
            # setattr
            ins = self.gettypefrom(v.get('type'),v.get('name'),
                     validators=v.get(
                         'validators'))
            print ins
            # inst = ins()
            setattr(MyFlaskForm, k,
                    ins)
        if 'submit' not in self.form.keys():
            setattr(MyFlaskForm, 'submit',
                    SubmitField('Submit'))
        return MyFlaskForm

    def gettypefrom(self, typename, name, validators):
        alltype = {
            'StringField': StringField(name, validators=validators),

        }
        print typename, alltype.get(typename)
        return alltype.get(typename)

    # def __str__(self):
    #     return '.......'

