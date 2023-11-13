"""Unittest Module for the Place Class"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up an instance of Place for reuse in test methods."""
        self.place = Place
        (
                city_id="123",
                user_id="456",
                name="Cozy Apartment",
                description="A comfortable place to stay",
                number_rooms=2,
                number_bathrooms=1,
                max_guest=4,
                price_by_night=100,
                latitude=37.7749,
                longitude=-122.4194,
                amenity_ids=["1", "2", "3"]
                )

    def test_place_instance(self):
        """Test if an instance of Place is created correctly."""
        place = self.place
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_place_attributes(self):
        """
        Test if attributes are set properly when creating a Place instance.
        """
        place = self.place
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.description, "A comfortable place to stay")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["1", "2", "3"])

    def test_place_to_dict(self):
        """Test the to_dict method of Place."""
        place = self.place
        place_dict = place.to_dict()

        self.assertEqual(place_dict['city_id'], "123")
        self.assertEqual(place_dict['user_id'], "456")
        self.assertEqual(place_dict['name'], "Cozy Apartment")
        self.assertEqual(
                place_dict['description'], "A comfortable place to stay")
        self.assertEqual(place_dict['number_rooms'], 2)
        self.assertEqual(place_dict['number_bathrooms'], 1)
        self.assertEqual(place_dict['max_guest'], 4)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 37.7749)
        self.assertEqual(place_dict['longitude'], -122.4194)
        self.assertEqual(place_dict['amenity_ids'], ["1", "2", "3"])
        self.assertEqual(place_dict['__class__'], "Place")

    def test_place_str(self):
        """Test the __str__ method of Place."""
        place = self.place
        place_str = str(place)

        self.assertIn('Place', place_str)
        self.assertIn(place.id, place_str)
        self.assertIn('Cozy Apartment', place_str)
        self.assertIn('A comfortable place to stay', place_str)


if __name__ == '__main__':
    unittest.main()
