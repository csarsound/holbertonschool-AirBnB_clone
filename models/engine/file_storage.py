#!/usr/bin/python3
"""This is the File Storage module.
Contains the FileStorage class.
"""
import json
from os import path

from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """This class serializes and deserializes instances to JSON and vice-versa.
    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): will store all objects by <class name>.id.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.
        Args:
            obj: the object to set in.
        """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = FileStorage.__objects.copy()
        output = {key: value.to_dict() for key, value in obj_dict.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(output, file, sort_keys=True, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                input = json.load(file)
                for key, value in input.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except:
            pass
