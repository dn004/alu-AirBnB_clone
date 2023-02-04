#!/usr/bin/python3
import unittest
from datetime import datetime

from time import sleep

from models.base_model import BaseModel


class TestCaseBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        print(self.my_model)
        sleep(1)
        self.my_model.save()
        print(self.my_model)
        my_model_json = self.my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    def test_to_dict(self):
        self.assertEqual(type(self.my_model.to_dict()), dict)

    def test_save(self):
        self.assertEqual(type(self.my_model.to_dict()['updated_at']),
                         type(self.my_model.to_dict()['created_at']))

    def test__str__(self):
        self.assertEqual(type(self.my_model.to_dict()['__class__']), str)
