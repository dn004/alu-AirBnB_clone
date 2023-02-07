#!/usr/bin/python3

#state

import unittest
import pep8import models
from models.state import State
from datetime import datetime
from io import StringIO
from contextlib import redirect_stdout



class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_state_init(self):
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state.name, str)
        self.assertEqual(self.state.name, "")

    def test_name_getter(self):
        self.state.name = "Enugu"
        self.assertEqual(self.state.name, "Enugu")
    def test_name_setter(self):
        self.state.name = "Lagos"
        self.assertEqual(self.state.name, "Lagos")

    def test_state_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
    unittest.main()
