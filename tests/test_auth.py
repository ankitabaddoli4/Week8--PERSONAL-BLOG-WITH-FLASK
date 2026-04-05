import unittest
from app import create_app, db
from app.models import User

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def test_register(self):
        response = self.client.post('/auth/register', data={
            'username': 'test',
            'email': 'test@test.com',
            'password': '123456'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
