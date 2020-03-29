from unittest import TestCase
import json

from config import TestingConfig
from app import create_app, db


LUFFY = {
    'email': 'luffy@grandline.pk',
    'username': 'Moneky D. Luffy',
    'password': 'ilovemeat'
}

ZORO = {
    'email': 'roronoa@grandline.bs',
    'password': 'gottatrain'
}


class UserAuthActionsTestCase(TestCase):
    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client

        with self.app.app_context():
            # create all db tables
            db.create_all()

    def test_user_signup_then_logout_then_login(self):
        client = self.client()
        new_user = self.signup(client, LUFFY)
        current_user = self.whoami(client, True)
        self.assertEqual(new_user, current_user)
        self.logout(client)
        self.whoami(client, False)
        login_user = self.login(client, new_user['email'], 'ilovemeat')
        self.assertEqual(new_user, login_user)

    def whoami(self, client, is_authenticated):
        r = client.get('/api/whoami')
        self.assertEqual(r.status_code, 200)
        res = r.get_json()
        self.assertEqual(is_authenticated, res['is_authenticated'])
        return res

    def signup(self, client, user, should_fail=False):
        """Signup a new user"""
        r = client.post('/api/signup', data={'user': json.dumps(user)})
        self.assertEqual(200, r.status_code)
        res = r.get_json()
        if should_fail:
            self.assertIn('error', res)
        else:
            self.assertEqual(user['email'], res['email'])
        return res

    def login(self, client, email, password, should_fail=False):
        """Login an existing user"""
        user = {'email': email, 'password': password}
        r = client.post('/api/login', data={'user': json.dumps(user)})
        self.assertEqual(200, r.status_code)
        res = r.get_json()
        if should_fail:
            self.assertIn('error', res)
        else:
            self.assertEqual(user['email'], res['email'])
        return res

    def logout(self, client):
        """Logout an user"""
        r = client.post('/api/logout')
        self.assertEqual(200, r.status_code)
        res = r.get_json()
        self.assertFalse(bool(res))

    def tearDown(self):
        """Destroy all initialized variables and db"""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()