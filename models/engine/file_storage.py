#!/usr/bin/python3
#model


import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    #File storing
    __objects = {}
    __file_path = "file.json"

    def all(self):
        #returning dict object
        return self.__objects

    def new (self, obj):
        #sets in  __objects the obj with key
        key = f'{obj.__class__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        #serializing objects to json
        with open(self.__file_path, "w+", encoding='utf-8') as f:
            json.dump(self.__objects, f, indent=2)

    def reload(self):
        #deserializing objects to json
            if path.exists(self.__file_path):
                with open(self.__file_path, "r", encoding='utf-8') as j:
                    self.__objects = json.load(j)
                    items = self.__objects
                    for item in items.values():
                        name_of_class = itesm['__class__']
                        self.new(eval(name_of_class + "(** "+ str(items) + ")"))
