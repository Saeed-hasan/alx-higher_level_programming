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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ convert obj to dic then to json sting in file """
        filename = cls.__name__ + ".json"
        list_dic = []
        if list_objs is not None:
            for i in list_objs:
                list_dic.append(cls.to_dictionary(i))
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dic))

    @classmethod
    def from_json_string(json_string):
        """ json string to dic """
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)
