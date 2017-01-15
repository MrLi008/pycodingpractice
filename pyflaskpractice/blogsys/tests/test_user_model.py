import unittest
from app_blog import create_app, db
from app_blog.models import User
import time

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()

        self.app_context.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_passwrod('cat'))
        self.assertFalse(u.verify_passwrod('dog'))

    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_select_from_users(self):
        users = User.query.all()
        print users
        self.assertIsNotNone(users)

    def test_valid_confirmation_token(self):
        u = User(password='cat')
        db.session.add(u)
        db.session.commit()
        token = u.generat_confirmation_token()
        self.assertTrue(u.confirm(token))


    def test_invalid_confirmation_token(self):
        u1 = User(password='cat')
        u2 = User(password='dog')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_reset_token()
        self.assertFalse(u2.confirm(token))


    def test_expired_confirmation_token(self):
        u = User(password='cat')
        db.session.add(u)
        db.session.commit()
        token = u.generat_confirmation_token(1)
        time.sleep(2)
        self.assertFalse(u.confirm(token))


    def test_valid_reset_token(self):
        u = User(password='cat')
        db.session.add(u)
        db.session.commit()
        token = u.generate_reset_token()
        self.assertTrue(u.reset_password(token, 'dog'))
        self.assertTrue(u.verify_passwrod('dog'))

    def test_invalid_reset_token(self):
        u1 = User(password='cat')
        u2 = User(password='dog')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generat_confirmation_token()
        self.assertFalse(u2.reset_password(token, 'horse'))
        self.assertTrue(u2.verify_passwrod('dog'))


    def test_valid_email_change_token(self):
        u = User(email='952934650@qq.com', password='cat')
        db.session.add(u)
        db.session.commit()
        token = u.generate_email_change_token('1114378425@qq.com')
        self.assertTrue(u.change_email(token))
        print u.email
        self.assertTrue(u.email == '1114378425@qq.com')

    def test_invalid_email_change_token(self):
        u1 = User(email='952934650@qq.com', password='cat')
        u2 = User(email='1114378325@qq.com', password='dog')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_email_change_token('11@qq.com')
        self.assertFalse(u2.change_email(token))
        self.assertTrue(u2.email == '1114378325@qq.com')


    def test_duplicate_email_change_token(self):
        u1 = User(email='952934650@qq.com', password='cat')
        u2 = User(email='1114378325@qq.com', password='dog')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_email_change_token('952934650@qq.com')
        self.assertFalse(u2.change_email(token))
        self.assertTrue(u2.email == '1114378325@qq.com')

































