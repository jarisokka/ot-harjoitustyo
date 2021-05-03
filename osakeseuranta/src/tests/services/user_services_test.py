import unittest
from entities.user import User
from repositories.user_repository import user_repository
from services.user_services import user_services, InvalidCredentialsError, UsernameExistsError

class FakeUserDatabase:
    def __init__(self):
        user_repository.delete_all()
        self.user_test = User('Test', 'test123')
        user_repository.create(self.user_test)

class TestUserServices(unittest.TestCase):
    def setUp(self):
        FakeUserDatabase()

    def test_login_correct(self):
        test_user = user_services.login('Test', 'test123')
        self.assertEqual(test_user.username, 'Test')

    def test_login_false(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: user_services.login('Test', 'test')
            )

    def test_create_user_exist(self):
        self.assertRaises(
            UsernameExistsError,
            lambda: user_services.create_user('Test', 'test')
            )

    def test_create_user(self):
        test_user = user_services.create_user('New', 'new123')
        self.assertEqual(test_user.username, 'New')
