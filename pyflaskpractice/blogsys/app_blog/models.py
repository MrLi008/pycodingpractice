# coding=utf8

from werkzeug.security import check_password_hash, generate_password_hash
from app_blog import db, login_manager
from flask_login import UserMixin, AnonymousUserMixin

# confirm by token
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request

from datetime import datetime
import hashlib


class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')


    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW |
                     Permission.COMMENT |
                     Permission.WRITE_ARTICLES, True),
            'Moderator': (Permission.FOLLOW |
                          Permission.COMMENT |
                          Permission.WRITE_ARTICLES |
                          Permission.MODERATE_COMMENTS, True),
            'Administrator': (0xff, True)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)

            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
            print r

        db.session.commit()

    def __repr__(self):
        return '<Role: '+str(self.id)\
               +', name: '+str(self.name)\
               +', permissions: '+str(self.permissions)\
               +', default: '+str(self.default)+'>'


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    # confirm
    confirmed = db.Column(db.Boolean, default=False)

    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(32))

    posts = db.relationship('Post', backref='author', lazy='dynamic')


    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()

        for i in range(count):
            u = User(email=forgery_py.internet.email_address(),
                     username=forgery_py.internet.user_name(True),
                     password=forgery_py.lorem_ipsum.word(),
                     confirmed=True,
                     name=forgery_py.name.full_name(),
                     location=forgery_py.address.city(),
                     about_me=forgery_py.lorem_ipsum.sentence(),
                     member_since=forgery_py.date.date(True))

            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError, e:
                print 'in generate_fake: ', e
                db.session.rollback()



    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()

            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

        if self.email is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()

        # print self.role

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
        return s.dumps({'confirm': self.id})

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
        self.avatar_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()

        db.session.add(self)
        return True

    def can(self, permissions):
        return self.role is not None \
                and self.role.permissions&permissions == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def gravatar(self, size=100, default='identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'https://www.gavatar.com/avatar'

        myhash = self.avatar_hash or hashlib.md5(self.email.encode('utf-8')).hexdigest()

        return '{url}/{myhash}?s={size}&d={default}&r={rating}'. \
            format(url=url,
                   myhash=myhash,
                   size=size,
                   default=default,
                   rating=rating)


    def __repr__(self):
        try:
            strs = '<User id: ' +str(self.id)\
                   + ', username: ' + self.username\
                   + ', role_id: ' + str(self.role_id)\
                   + ', password_hash: ' + self.password_hash\
                   + ', email: ' + self.email\
                   + ', confirmed: '+ str(self.confirmed)\
                   + ', name: ' + self.name\
                   + '>'
        except TypeError, e:
            print e
            strs = 'wrong...'
        return strs


class AnonymousUser(AnonymousUserMixin):

    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py


        seed()
        user_count = User.query.count()
        for i in range(count):
            u = User.query.offset(randint(0, user_count - 1)).first()
            p = Post(body=forgery_py.lorem_ipsum.sentences(randint(1, 5)),
                     timestamp=forgery_py.date.date(True),
                     author=u)

            db.session.add(p)
            db.session.commit()


if __name__ == '__main__':
    db.create_all()