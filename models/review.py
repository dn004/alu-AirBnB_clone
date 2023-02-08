#!/usr/bin/python3

#module
from models.base_model import BaseModel

#class with attributes
class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
