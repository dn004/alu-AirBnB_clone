#!/usr/bin/python3

import uuid
from datetime import datetime
from models import models, storage

#defining all common attributes for other classes 
class BaseModel:
    #initialize
    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.fromisofrmat(v)
                    setattr(self, k, v)
                    continue
                if k!= '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):

        
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
    
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        #return dict
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = new_dict['update_at'].isoformat()
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        return new_dict
