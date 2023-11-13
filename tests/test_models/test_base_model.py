import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up a common instance for testing."""
        self.base_model = BaseModel()

    def test_attributes_on_creation(self):
        """Test if id, created_at, and updated_at are set on creation."""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        """Test if the id attribute is a string."""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """Test if the created_at attribute is a datetime object."""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if the updated_at attribute is a datetime object."""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of the instance."""
        expected_str = "[BaseModel] ({}) {}".format(
                self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_updates_updated_at(self):
        """Test if calling save updates the updated_at attribute."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary representation."""
        obj_dict = self.base_model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_datetime_format(self):
        """Test if the datetime attributes are formatted correctly"""
        obj_dict = self.base_model.to_dict()
        self.assertEqual(
                obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(
                obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_recreate_instance_from_dict(self):
        """Test if a new instance can be recreated from a dictionary."""
        obj_dict = self.base_model.to_dict()
        new_instance = BaseModel(**obj_dict)
        self.assertEqual(new_instance.id, self.base_model.id)
        self.assertEqual(new_instance.created_at, self.base_model.created_at)
        self.assertEqual(new_instance.updated_at, self.base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
