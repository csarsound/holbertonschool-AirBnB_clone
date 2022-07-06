#!/usr/bin/python3
""" This module contains a class FileStorage that serializes
    instances to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User

class FileStorage:
    """
    Class Storage
    """

    __objects = {}
    __file_path = "file.json"

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
            """ serializes __objects to the JSON file """
            empty_dict = {}
            for key, value in self.__objects.items():
                empty_dict[key] = value.to_dict()
            with open(self.__file_path, "w") as file:
                json.dump(empty_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                content = (json.load(file))
                for key, value in content.items():
                    class_name = value.get('__class__')
                    obj = eval(class_name + '(**value)')
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
