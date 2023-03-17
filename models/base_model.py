#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseClass that define al common Attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.updated_at = kwargs.get('updated_at', datetime.utcnow())
        self.created_at = kwargs.get('create_at', datetime.utcnow())
        models.storage.new(self)


    def __str__(self) -> str:
        """a method to implement object"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """instance method to update time """
        self.updated_at = datetime.utcnow()
        models.storage.save()


    def to_dict(self):
        """instance method to return dictionary containing all keys/values"""
        the_dict = self.__dict__.copy()
        the_dict['__class__'] = self.__class__.__name__
        the_dict['created_at'] = str(self.created_at.isoformat())
        the_dict['updated_at'] = str(self.updated_at.isoformat())
        return the_dict
