#config=utf8

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(Form):
    name = StringField('name: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

