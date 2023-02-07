#!/usr/bin/python3

#Tests for Place


import unittest
import pep8
import models
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    
    def setUp(self):
        self.place = Place()

    def test_city_id(self):
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        self.assertIsInstance(self.place.user_id, str)
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        self.assertIsInstance(self.place.name, str)
        self.assertEqual(self.place.name, "")

    def test_description(self):
        self.assertIsInstance(self.place.description, str)
        self.assertEqual(self.place.description, "")
    
    def test_latitude(self):
        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.latitude, 0.0)
    def test_longitude(self):
        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.place.longitude, 0.0)


    def test_number_bathrooms(self):
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 0)
    def test_number_rooms(self):
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertEqual(self.place.number_rooms, 0)

    def test_max_guest(self):
        self.assertIsInstance(self.place.max_guest, int)
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertEqual(self.place.price_by_night, 0)

    def test_amenity_ids(self):
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
    unittest.main()
