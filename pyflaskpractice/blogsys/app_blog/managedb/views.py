from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from .. import db
from ..models import Permission, Role, User, Post, Comment, BD
from ..decorators import admin_required, permission_required
from . import managedb
from wtforms.validators import DataRequired
import forms
from constructionflaskform import ConstructionFlaskForm

@managedb.route('/', methods=['GET','POST'])
def index():
    form = forms.BaseData()
    if request.method == 'POST':
        print 'in post'
        basedata = BD(
            db_name=form.db_name.data,
            db_type=form.db_type.data,
            db_default=form.db_default.data,
            db_pri=form.db_pri.data,
        )
        db.session.add(basedata)

    bdlist = BD.query.all()
    dbdict = []
    for bd in bdlist:

        params = {
            str(bd.id): {
                'type': 'StringField',
                'name': bd.db_name,
                'validators': [DataRequired()]
            }
        }
        cf = ConstructionFlaskForm(params=params)
        # print cf
        # print cf.MyFlaskForm.__dict__
        newform = cf.convertdicttowtfform()()
        dbdict.append(newform)



    return render_template('managedb/index.html', form=form, dbdict=dbdict)