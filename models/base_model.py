#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """BaseClass that define al common Attributes/methods for other classes"""

    def __init__(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                key = value
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self) -> str:
        """a method to implement object"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """instance method to update time """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """instance method to return dictionary containing all keys/values"""
        the_dict = self.__dict__.copy()
        the_dict['__class__'] = self.__class__.__name__
        the_dict['self.created_at'] = self.created_at.isoformat()
        the_dict['self.updated_at'] = self.updated_at.isoformat()
        return the_dict
