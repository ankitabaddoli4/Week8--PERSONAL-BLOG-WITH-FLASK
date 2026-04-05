import unittest
from app import create_app, db
from app.models import User

class PostTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            user = User(username='test', email='test@test.com')
            user.set_password('123')
            db.session.add(user)
            db.session.commit()

    def test_create_post_page(self):
        response = self.client.get('/posts/create')
        self.assertEqual(response.status_code, 302)  # redirect (login required)