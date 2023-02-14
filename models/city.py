#!/usr/bin/python3
"""
This script defines a class City which inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines a class which inherits from BaseModels.
    Attributes:
        state_id (str): empty string
        name (str): empty string
    """
    state_id = ""
    name = ""
