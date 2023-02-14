#!/usr/bin/python3
import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
"""
Defines a class ``FileStorage``.
"""


class FileStorage:
    """
    ``FileStorage class serializes instances to a JSON file,
    and deserializes JSON file to instances.
    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): stores all objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            dict_new = {}
            for key, value in self.__objects.items():
                dict_new[key] = value.to_dict()
            json.dump(dict_new, f)

    def reload(self):
        """
        Deserializes the JSON file to __object, only if the
        __file_path exists
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as f:
                outer_dict = json.load(f)
                for value in outer_dict.values():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value))
