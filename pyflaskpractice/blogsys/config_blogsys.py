# coding=utf8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class ConfigBlogSys:
    SECRET_KEY ='hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = '25'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '952934650@qq.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWOED', 'puspepdqiwiobefe')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky MrLi <952934650@qq.com>'
    FLASKY_ADMIN = '952934650@qq.com'
    FLASKY_FOLLOWERS_PER_PAGE=3

    FLASKY_POSTS_PER_PAGE = 2

    FLASKY_COMMENTS_PER_PAGE = 3

    @staticmethod
    def init_app(app):
        print 'This is in init_app', app


class DevelopmentConfig(ConfigBlogSys):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(ConfigBlogSys):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(ConfigBlogSys):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config_blogsys = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    # default
    'default': DevelopmentConfig
}
