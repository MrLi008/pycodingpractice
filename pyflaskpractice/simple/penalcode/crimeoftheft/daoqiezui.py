# coding=utf8


from flask import Flask, render_template, redirect, session, url_for, flash


from flask_bootstrap import Bootstrap
from flask_moment import Moment


# form
from flask_wtf.form import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, RadioField, BooleanField


from filterprocess import res_re

from benchmark_punishment import getSentencingRange_API

app = Flask(__name__)
# manage = Manager(app)
moment = Moment(app)
bootstrap = Bootstrap(app)


class DataForm(FlaskForm):
    chpre = RadioField(u'项目选择')
    b = BooleanField(u'复选框')
    submit = SubmitField(u'提交')

    # for k in res_re.keys():
    #     l.append(SelectMultipleField(k, choices= ))





@app.route('/', methods=['GET', 'POST'])
def index():
    form_left = DataForm()




    if not session.has_key('flag'):
        session['flag'] = 1

        session['postdata'] = dict()
        session['nowproj'] = None
        session['choices'] = [(k, k) for k in res_re.keys()]

    # 设定选择列
    form_left.chpre.choices = session['choices']

    if form_left.validate_on_submit():


        proj = form_left.chpre.data

        print 'proj: ', proj
        if session['flag'] == 1:
            flash('Looks like you have post some data')
            session['flag'] = 2
            session['nowproj'] = proj
            if not session['postdata'].has_key(session['nowproj']):
                session['postdata'][session['nowproj']] = ''

            session['choices'] = [(vk, vk) for vk in res_re.get(session['nowproj'])]



            # return render_template('index.html', form=form_left, proj=proj)
            return  redirect(url_for('index'))
        elif session['flag'] == 2:
            session['flag'] = 1
            flash('looks like .....')
            session['postdata'][session['nowproj']] = proj
            session['choices'] = [(vk, vk) for vk in res_re.keys()
                                  if vk not in session['postdata']]

            return redirect(url_for('index'))


    return render_template('index.html', form=form_left, res_re=res_re)

# manager = Manager(app)

# app config
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'

if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()

    # app_context = app.app_context()
    # app_context.push()
    #
    #
    # print current_app.name











