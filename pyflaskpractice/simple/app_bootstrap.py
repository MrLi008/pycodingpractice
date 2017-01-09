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

class NameForm(FlaskForm):
    name = StringField('What is your name:', validators=[DataRequired()])
    submit = SubmitField('Submit')





app = Flask(__name__)
# manage = Manager(app)
moment = Moment(app)
bootstrap = Bootstrap(app)



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

app.config['SECRET_KEY'] = 'hard to guess string'


if __name__ == '__main__':
    # manage.run()
    app.run()





