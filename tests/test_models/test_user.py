#!/usr/bin/python3


import unittest
import pep8
from datetime import datetime
import models
from models.user import User
from io import StringIO
from contextlib import redirect_stdout


class TestUser(unittest.TestCase):
    def test_class(self):
        """creating object and testing class user"""
        user = User()
        self.assertEqual(user.__class__.__name__, "User")
    
    def setUp(self):
        self.user = User()

    def test_last_name(self):
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "")
    def test_first_name(self):
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "")

    def test_email(self):
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "")

    def test_password(self):
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "")

    def test_user_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
    unittest.main()
