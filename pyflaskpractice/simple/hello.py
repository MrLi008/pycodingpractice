# coding=utf8

from flask import Flask
from flask import request
from flask import current_app
from flask import redirect
from flask import abort
from flask import make_response


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!!</h1>'

@app.route('/user/<name>')
def user2(name):
    return '<h1>Hello, %s!</h1>' %name

@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' %user_agent

@app.route('/redirect/<url>')
def redirect_to(url):
    return redirect('http://'+url)

@app.route('/user/<id>')
def get_user(id):
    user = True
    if not user:
        abort(404)
    return '<h1>Hi, %s</h1>' %id

@app.route('/res')
def res():
    response = make_response('<h1>This document carries a cookie!!</h1>')
    response.set_cookie('answer', '42')
    return response





if __name__ == '__main__':
    app.run(debug=True)

    print current_app.name









