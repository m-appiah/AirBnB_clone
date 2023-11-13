"""Unittest Module for the Amenity Class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Set up an instance of Amenity for reuse in test methods."""
        self.amenity = Amenity()

    def test_amenity_instance(self):
        """Test if an instance of Amenity is created correctly."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attributes(self):
        """Test if attributes are set properly when creating an instance."""
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_to_dict(self):
        """Test the to_dict method of Amenity."""
        amenity = Amenity(name="Gym")
        amenity_dict = amenity.to_dict()

        self.assertEqual(amenity_dict['name'], "Gym")
        self.assertEqual(amenity_dict['__class__'], "Amenity")

    def test_amenity_str(self):
        """Test the __str__ method of Amenity."""
        amenity = Amenity(name="Pool")
        amenity_str = str(amenity)

        self.assertIn('Amenity', amenity_str)
        self.assertIn(amenity.id, amenity_str)
        self.assertIn('name', amenity_str)
        self.assertIn("Pool", amenity_str)


if __name__ == '__main__':
    unittest.main()
