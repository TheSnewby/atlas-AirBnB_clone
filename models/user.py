#!/usr/bin/python3
"""
User class module for AirBnB clone
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Beginning stage of User class

    Attributes:
        email (str):      user email
        password (str):   user password
        first_name (str): user first name
        last_name (str):  user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
