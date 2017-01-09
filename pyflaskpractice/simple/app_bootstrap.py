# coding=utf8

from flask import Flask, render_template, redirect, session, url_for, flash

from flask_script import Manager

from flask_bootstrap import Bootstrap
from flask_moment import Moment

from datetime import datetime

# form
from flask_wtf.form import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_migrate import Migrate, MigrateCommand
from flask_email import EmailMessage


# self module
import data_module
import sqlconfig

class NameForm(FlaskForm):
    name = StringField('What is your name:', validators=[DataRequired()])
    message = StringField('Input your message: ', validators=[DataRequired()])
    submit = SubmitField('Submit')





app = Flask(__name__)
# manage = Manager(app)
moment = Moment(app)
bootstrap = Bootstrap(app)

db = sqlconfig.config_sql(app)


@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/base')
def base():
    return render_template('base.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/get', methods=['GET', 'POST'])
def get_data():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        print 'your old input: ', old_name, form.name.data
        if old_name is not None and old_name != form.name.data:
            print 'it is not same'

            flash('Looks like you have changed your name!')

        session['name'] = form.name.data
        return redirect(url_for('get_data'))

    return render_template('get.html', form=form, name=session.get('name'))

count = 0

@app.route('/login', methods=['GET', 'POST'])
def login():
    global count
    form = NameForm()
    if form.validate_on_submit():
        user = data_module.User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = data_module.User(username=form.name.data)

            db.session.add(user)
            session['Known'] = False
        else:
            count += 1
            session['Known'] = True

        session['name'] = form.name.data
        form.name.data = ''

    return render_template("login.html",
                           form = form,
                           name = session.get('name'),
                           known = session.get('Known', False),
                           count=count)

@app.route('/sendto', methods=['GET', 'POST'])
def sendto():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        message = form.message.data
        if name is None or message is None:
            flash('please input your name and message')



    session['message'] = form.name.data
    return render_template('sendto.html',
                           form=form,
                           name=session.get('name', 'no name'),
                           message=session.get('message', 'no message'))







# app config
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'




# migrate = Migrate(app, db)
# manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # manage.run()
    app.run()





