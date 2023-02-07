#!/usr/bin/python3
"""
Amenity
"""

import unittest
import pep8
from datetime import datetime
import models
from models.amenity import Amenity
from io import StringIO
from contextlib import redirect_stdout



class TestAmenity(unittest.TestCase):

#Testing

    def setUp(self):
#setup
        self.amenity = Amenity()

    def test_amenity_init(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(self.amenity.name, "")

    def test_name_getter(self):
        self.amenity.name = "Electricity"
        self.assertEqual(self.amenity.name, "Electricity")
    def test_name_setter(self)
        self.amenity.name = "Internet"
        self.assertEqual(self.amenity.name, "Internet")

    def test_amenity_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
    unittest.main()
