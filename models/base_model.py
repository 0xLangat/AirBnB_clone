#!/usr/bin/python3
import uuid
from datetime import datetime
"""This module defines all common attributes.

The methods/attributes for other classes start here.
It defines a class ``BaseModel``
"""


class BaseModel:
    """A base model that has common attribute/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the basemodel class."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Return the string representation of an object."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute update_at,
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__,
        of the instance.
        """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
