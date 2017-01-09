# coding=utf8

'''
u'
数据库配置信息以及初始化
'
'''


import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# print SQLAlchemy.__version__

basedir = os.path.abspath(os.path.dirname(__file__))

baseModule = declarative_base()

def config_sql(app):
    if app is None:
        return None

    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db = SQLAlchemy(app)

    return db



















