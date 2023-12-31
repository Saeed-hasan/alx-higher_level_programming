#!/usr/bin/python3
"""
Module-8:rectangle
inherince from base_geometry

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ contain the init method """
    def __init__(self, width, height):
        """ init the width and height """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
