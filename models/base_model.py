#!/usr/bin/python3
"""This is the Base Model module.
Contains the BaseModel class which will be the
"base" of all other classes in this project.
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    The goal is to manage all common attributes and methods for other classes.
    Attributes:
        id (str): unique random ID for each BaseModel instance.
        created_at (datetime): the current datetime when instance is created.
        updated_at (datetime): the current datetime when instance is updated.
    """

    def __init__(self, *args, **kwargs):
        """ Constructor """

        for key, value in kwargs.items():
            if key == "__class__":
                continue

            if (key == "created_at" or key == "updated_at"):
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

            setattr(self, key, value)

        if "id" not in kwargs.keys():
            self.id = str(uuid4())

        if "created_at" not in kwargs.keys():
            self.created_at = datetime.now()

        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.now()

    def __str__(self):
        """overrides the default behaviour of the __str__ method."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with all the keys/value of the instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.create_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
