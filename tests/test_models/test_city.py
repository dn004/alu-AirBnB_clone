#!/usr/bin/python3

#City


import unittest
import pep8
import models
from models.city import City
from datetime import datetime



class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_city_init(self):
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_name_getter(self):
        self.city.name = "Port Harcourt"
        self.assertEqual(self.city.name, "Port Harcourt")
    def test_name_setter(self):
        self.city.name = "Onitsha"
        self.assertEqual(self.city.name, "Onitsha")

    def test_city_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
    unittest.main()
