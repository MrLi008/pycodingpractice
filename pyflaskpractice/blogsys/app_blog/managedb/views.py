from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from .. import db
from ..models import Permission, Role, User, Post, Comment, BD
from ..decorators import admin_required, permission_required
from . import managedb
import forms

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
    dbdict = {}
    for bd in bdlist:
        if bd.db_pri in dbdict.keys():
            dbdict[bd.db_pri] = []

        dbdict[bd.bd.db_pri].append(bd)


    return render_template('managedb/index.html', form=form, dbdict=dbdict)