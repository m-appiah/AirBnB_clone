"""Unittest Module for FileStorage class"""

import unittest
from models.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up the FileStorage instance for testing."""
        self.file_storage = FileStorage()

    def tearDown(self):
        """Clean up by removing the test file if it exists."""
        test_file_path = "test_file.json"
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

    def test_all_method(self):
        """Test the all method of FileStorage."""
        all_objects = self.file_storage.all()
        self.assertEqual(len(all_objects), 0)

        user = User()
        state = State()
        city = City()
        place = Place()
        amenity = Amenity()
        review = Review()

        self.file_storage.new(user)
        self.file_storage.new(state)
        self.file_storage.new(city)
        self.file_storage.new(place)
        self.file_storage.new(amenity)
        self.file_storage.new(review)

        # Check if all the instances are in the dictionary
        all_objects = self.file_storage.all()
        self.assertEqual(len(all_objects), 6)
        self.assertIn("User." + user.id, all_objects)
        self.assertIn("State." + state.id, all_objects)
        self.assertIn("City." + city.id, all_objects)
        self.assertIn("Place." + place.id, all_objects)
        self.assertIn("Amenity." + amenity.id, all_objects)
        self.assertIn("Review." + review.id, all_objects)

    def test_new_method(self):
        """Test the new method of FileStorage."""
        # Ensure initially there are no objects
        all_objects = self.file_storage.all()
        self.assertEqual(len(all_objects), 0)

        # Create a test instance and add it to FileStorage
        user = User()
        self.file_storage.new(user)

        # Check if the instance is in the dictionary
        all_objects = self.file_storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn("User." + user.id, all_objects)

    def test_save_and_reload_methods(self):
        """Test the save and reload methods of FileStorage."""
        # Create a test instance and add it to FileStorage
        user = User()
        self.file_storage.new(user)

        # Save the instances to a test file
        self.file_storage.save()

        # Create a new FileStorage instance and reload from the test file
        new_file_storage = FileStorage()
        new_file_storage.reload()

        # Check if the reloaded instance is in the dictionary
        all_objects = new_file_storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn("User." + user.id, all_objects)

    def test_reload_method_nonexistent_file(self):
        """Test the reload method when the file does not exist."""
        new_file_storage = FileStorage()
        new_file_storage.reload()

        all_objects = new_file_storage.all()
        self.assertEqual(len(all_objects), 0)


if __name__ == '__main__':
    unittest.main()
