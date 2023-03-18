#!/usr/bin/python3
"""Defines FileStorage class."""
import pickle

class FileStorage:
    """A class that serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json" # path to the JSON file
    __objects = {} # dictionary that will store all objects by <class name>.id

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "wb") as f:
            pickle.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        try:
            with open(self.__file_path, "rb") as f:
                self.__objects = pickle.load(f)
        except FileNotFoundError:
            pass
