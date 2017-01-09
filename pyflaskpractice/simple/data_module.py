# coding=utf8

import sqlconfig
# from app_bootstrap import app
from flask import Flask

app = Flask(__name__)

db = sqlconfig.config_sql(app)

baseModule = sqlconfig.baseModule


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User '+self.username+' '+str(self.id)+'>\n'




if __name__ == '__main__':
    admin = User(username='admin16')

    db.create_all()
    # db.session.add(admin)
    # db.session.commit()

    # print admin.id, admin

    # admin.username += admin.username
    # admin.id = 0
    # db.session.add(admin)
    # db.session.commit()

    print admin.id, admin.username
    print User.query.all()
    print User.query.filter_by(username='admin15admin15').all()
    db.session.close()



