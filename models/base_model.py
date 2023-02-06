#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

""" defining all common attributes/methods for other classes """


class BaseModel:
    
    """initialize class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, v in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                    continue
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ represent
        as string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """update to current time"""
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """return dictionary
        with all values """
        the_dict = self.__dict__.copy()
        the_dict['__class__'] = self.__class__.__name__
        the_dict['self.created_at'] = self.created_at.isoformat()
        the_dict['self.updated_at'] = self.updated_at.isoformat()
        return the_dict
