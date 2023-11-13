"""Unittest Module for the City Class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up an instance of City for reuse in test methods."""
        self.city = City(state_id="CA", name="San Francisco")

    def test_city_instance(self):
        """Test if an instance of City is created correctly."""
        city = self.city
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        """Test if attributes are set properly when creating instance."""
        city = self.city
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_city_to_dict(self):
        """Test the to_dict method of City."""
        city = self.city
        city_dict = city.to_dict()

        self.assertEqual(city_dict['state_id'], "CA")
        self.assertEqual(city_dict['name'], "San Francisco")
        self.assertEqual(city_dict['__class__'], "City")

    def test_city_str(self):
        """Test the __str__ method of City."""
        city = self.city
        city_str = str(city)

        self.assertIn('City', city_str)
        self.assertIn(city.id, city_str)
        self.assertIn('state_id', city_str)
        self.assertIn('name', city_str)
        self.assertIn("San Francisco", city_str)


if __name__ == '__main__':
    unittest.main()
