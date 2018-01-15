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

        return redirect(url_for('managedb.index'))
    return render_template('managedb/index.html', form=form)

@managedb.route('/<id>', methods=['POST', 'GET'])
def release(id):
    ins = BD.query.get_or_404(id)


    return render_template('managedb/release.html', ins=ins)



@managedb.route('/all', )
def alldata():
    al = BD.query.all()
    print 'length of al: ', len(al)

    for a in al:
        print a.id

    return 'all data'


