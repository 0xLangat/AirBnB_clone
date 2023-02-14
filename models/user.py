#!/usr/bin/python3
from models.base_model import BaseModel
"""
This script contains a class ``User`` that inherits from,
``BaseModel``.
"""


class User(BaseModel):
    """
    The class inherits from the BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
