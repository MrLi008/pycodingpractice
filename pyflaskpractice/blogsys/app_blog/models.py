# coding=utf8

from werkzeug.security import check_password_hash, generate_password_hash
from app_blog import db, login_manager
from flask_login import UserMixin

# confirm by token
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role '+str(self.id)+','+self.name+','+self.users+'>'


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    # confirm
    confirmed = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        # self.password_hash = password


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
        # return True


    def generat_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm':self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception, e:
            print 'in confirm: ', e

            return False

        if data.get('confirm') != self.id:
            return False

        self.confirmed = True
        db.session.add(self)

        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception, e:
            print 'in reset password: ', e
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)

        return True
    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception,e:
            print 'in change email: ', e
            return False

        if data.get('change_email') != self.id:
            print 'change_email id != self.id'
            return False
        new_email = data.get('new_email')
        if new_email is None:
            print 'new email is None.'
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            print 'select email is not None'
            return False
        self.email = new_email
        db.session.add(self)
        return True



    def __repr__(self):
        return '<User '+str(self.id)+','+self.username+','+str(self.role_id)+','+self.password_hash+'>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    db.create_all()