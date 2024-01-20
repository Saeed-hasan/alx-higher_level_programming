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

    @staticmethod
    def from_json_string(json_string):
        """ load json from file """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        instances = []
        try:
            text = []
            with open(filename, 'r') as f:
                text = cls.from_json_string(f.read())
                for obj in text:
                    instances.append(cls.create(**obj))
        except FileNotFoundError:
            instances = []

        return instances
