"""Unittest module for User Class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_user_instance_creation(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_str_method(self):
        user = User()
        user_str = str(user)
        self.assertIn('User', user_str)
        self.assertIn(user.id, user_str)
        self.assertIn('email', user_str)
        self.assertIn('password', user_str)
        self.assertIn('first_name', user_str)
        self.assertIn('last_name', user_str)

    def test_user_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")

    def test_user_save_method(self):
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)


if __name__ == '__main__':
    unittest.main()
