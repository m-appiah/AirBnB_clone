#!/usr/bin/python3
"""
Defines the unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
from datetime import datetime
from time import sleep
from models.place import Place
import os
import models
import unittest


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(placel))
        self.assertNotIn("city_id", placel.__dict__)

    def test_user_id_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(placel))
        self.assertNotIn("user_id", placel.__dict__)

    def test_name_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(placel))
        self.assertNotIn("name", placel.__dict__)

    def test_description_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(placel))
        self.assertNotIn("desctiption", placel.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(placel))
        self.assertNotIn("number_rooms", placel.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(placel))
        self.assertNotIn("number_bathrooms", placel.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(placel))
        self.assertNotIn("max_guest", placel.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(placel))
        self.assertNotIn("price_by_night", placel.__dict__)

    def test_latitude_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(placel))
        self.assertNotIn("latitude", placel.__dict__)

    def test_longitude_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(placel))
        self.assertNotIn("longitude", placel.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        placel = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(placel))
        self.assertNotIn("amenity_ids", placel.__dict__)

    def test_two_places_unique_ids(self):
        placel1 = Place()
        placel2 = Place()
        self.assertNotEqual(placel1.id, placel2.id)

    def test_two_places_different_created_at(self):
        placel1 = Place()
        sleep(0.05)
        placel2 = Place()
        self.assertLess(placel1.created_at, placel2.created_at)

    def test_two_places_different_updated_at(self):
        placel1 = Place()
        sleep(0.05)
        placel2 = Place()
        self.assertLess(placel1.updated_at, placel2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        placel = Place()
        placel.id = "123456"
        placel.created_at = placel.updated_at = dt
        placelstr = placel.__str__()
        self.assertIn("[Place] (123456)", placelstr)
        self.assertIn("'id': '123456'", placelstr)
        self.assertIn("'created_at': " + dt_repr, placelstr)
        self.assertIn("'updated_at': " + dt_repr, placelstr)

    def test_args_unused(self):
        placel = Place(None)
        self.assertNotIn(None, placel.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        placel = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(placel.id, "345")
        self.assertEqual(placel.created_at, dt)
        self.assertEqual(placel.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        placel = Place()
        sleep(0.05)
        first_updated_at = placel.updated_at
        placel.save()
        self.assertLess(first_updated_at, placel.updated_at)

    def test_two_saves(self):
        placel = Place()
        sleep(0.05)
        first_updated_at = placel.updated_at
        placel.save()
        second_updated_at = placel.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        placel.save()
        self.assertLess(second_updated_at, placel.updated_at)

    def test_save_with_arg(self):
        placel = Place()
        with self.assertRaises(TypeError):
            placel.save(None)

    def test_save_updates_file(self):
        placel = Place()
        placel.save()
        placelid = "Place." + placel.id
        with open("file.json", "r") as f:
            self.assertIn(placelid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        placel = Place()
        self.assertIn("id", placel.to_dict())
        self.assertIn("created_at", placel.to_dict())
        self.assertIn("updated_at", placel.to_dict())
        self.assertIn("__class__", placel.to_dict())

    def test_to_dict_contains_added_attributes(self):
        placel = Place()
        placel.middle_name = "Holberton"
        placel.my_number = 98
        self.assertEqual("Holberton", placel.middle_name)
        self.assertIn("my_number", placel.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        placel = Place()
        placel_dict = placel.to_dict()
        self.assertEqual(str, type(placel_dict["id"]))
        self.assertEqual(str, type(placel_dict["created_at"]))
        self.assertEqual(str, type(placel_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        placel = Place()
        placel.id = "123456"
        placel.created_at = placel.updated_at = dt
        tdict = {
                'id': '123456',
                '__class__': 'Place',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                }
        self.assertDictEqual(placel.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        placel = Place()
        self.assertNotEqual(placel.to_dict(), placel.__dict__)

    def test_to_dict_with_arg(self):
        placel = Place()
        with self.assertRaises(TypeError):
            placel.to_dict(None)


if __name__ == "__main__":
    unittest.main()
