#!/usr/bin/python3

#model
from models.base_model import BaseModel

#A class with 4 attributes

class User(BaseModel):
    email = ""
    password = ""
    last_name = ""
    first_name = ""
