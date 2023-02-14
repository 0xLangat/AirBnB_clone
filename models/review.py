#!/usr/bin/python3
"""
This script defines a class that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines the class Review which inherits from BaseModel.
    Attributes:
        place_id (str): empty string
        user_id (str): empty string
        text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""
