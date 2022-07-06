#!/usr/bin/python3
"""
Unittesting module for BaseModel class
"""
import models
from models.base_model import BaseModel
import os
import unittest
import datetime


class Test_Base_Model(unittest.TestCase):
    """
	Unittesting class
    """

    def test_datetime(self):
        """
        Checks for datetime attributes
        """
        #Test if two instnace has diferent datetime
        my_amenity = Amenity()
        my_amenity_2 = Amenity()
        self.assertNotEqual(my_amenity.created_at, my_amenity_2.created_at)
        self.assertNotEqual(my_amenity.updated_at, my_amenity_2.updated_at)

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
