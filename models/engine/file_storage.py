#!/usr/bin/python3
# serializing instances to json files and deserializing json files to instances

import json


class FileStorage:
# for storing files
    __objects = {}
    __file_path = "file.json"


    def __init__(self):
        # for instances

    def all(self):
        # returns the dictionary __objects
        return self.__objects

    def new (self, obj):
        # sets in __objects the obj with key <obj classname>.id
        key = f'{obj.__class__}.{obj.id}'
        self.__objects[key] = obj


    def save(self):
        # serializes __objects to the json file
        with open (self.__file_path, "w", encoding='utf-8') as f:
            json.dump(self.__objects, f, indent=2)


    def reload(self):
        # deserializes the json file to __objects
        with open(self.__file_path, "r", encoding='utf-8') as j:
            self.__objects = json.load(j)#!/usr/bin/python3
