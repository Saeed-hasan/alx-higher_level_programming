#!/usr/bin/python3
"""module base"""
import json


class Base:
    """ Class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ dic to json string """
        if list_dictionaries is None and len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
