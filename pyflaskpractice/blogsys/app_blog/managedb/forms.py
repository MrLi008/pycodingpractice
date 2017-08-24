#config=utf8

from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from app_blog.models import Role, User

class BaseData(FlaskForm):
    db_name = StringField('name', validators=[DataRequired()])
    db_type = StringField('type', validators=[DataRequired()])
    db_default = StringField('default_value', validators=[DataRequired()])

    db_pri = IntegerField('privilage', validators=[DataRequired()])
    db_pre = StringField('pre node', validators=[DataRequired()])

    submit = SubmitField('Submit')