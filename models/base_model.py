#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"""
This module defines a class ``BaseModel``.

``BaseModel`` defines all common attributes/methods for other classes.

"""


class BaseModel:
    """
    Represents a class ``BaseModel``.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the instance of class ``BaseModel``.

        Args:
            *args (any): variable number of arguments
            **kwargs (any): variable number of key/value arguments
        Attributes:
            id (str): unique ID for the object
            created_at (any): current datetime when an instance is created.
            updated_at (any): current datetime when an instance is created,
                    any it will be updated everytime the object is changed.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of an object.
        """

        return f"[{self.__class__.__name__}] ({self.id} {self.__dict__})"

    def save(self):
        """
        Updates the public instance attribute  ``updated_at,
        with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__,
        of the instance.
        - by using self.__dict__, only instance attributes set will be returned
        - a key __class__ must be added to the dict with the class name
        - created_at and updated_at must be converted to string object
        """
        get_dict = dict(self.__dict__)
        get_dict["__class__"] = self.__class__.__name__

        for key, value in get_dict.items():
            if key == "created_at" or key == "updated_at":
                get_dict[key] = value.isoformat()

        return get_dict
