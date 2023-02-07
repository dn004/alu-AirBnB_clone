#!/usr/bin/python3

#models

import unittest
import pep8
import models
from models.review import Review
from datetime import datetime



class TestReview(unittest.TestCase):
    
    def setUp(self):
        self.review = Review()

    def test_user_id(self):
        self.assertIsInstance(self.review.user_id, str)
        self.assertEqual(self.review.user_id, "")
    def test_place_id(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertEqual(self.review.place_id, "")

    def test_text(self):
        self.assertIsInstance(self.review.text, str)
        self.assertEqual(self.review.text, "")

    def test_review_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
    unittest.main()
