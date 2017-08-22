# coding=utf8

'''
app factory
init
'''

from flask import Flask
from flask_bootstrap import Bootstrap

from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown


from config_blogsys import config_blogsys

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

# login manager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    # app.config['DEBUG'] = True

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.config.from_object(config_blogsys[config_name])
    config_blogsys[config_name].init_app(app)

    # register
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    # login
    login_manager.init_app(app)

    pagedown.init_app(app)


    # register mainofindex
    # import app_blog.mainofindex as mfi
    from app_blog.mainofindex import mainofindex
    # print app
    # print mainofindex
    app.register_blueprint(mainofindex)

    # register auth
    from app_blog.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    # register managedb
    from app_blog.managedb import managedb
    app.register_blueprint(managedb, url_prefix='/managedb')

    return app




