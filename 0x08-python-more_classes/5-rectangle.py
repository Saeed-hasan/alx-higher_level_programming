#!/usr/bin/python3
"""
Module_5 rectangle
Contains class Rectangle with private attributes,
public area and perimeter methods, and allows printing #'s
"""


class Rectangle:
    """
    Defines class rectangle with private attribute

    Args:
        width (int): width
        height (int): height
    """
    def __init__(self, width=0, height=0):
        """ Initializion"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter  """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Return perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.height)

    def __str__(self):
        """ Prints rectangle  """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
                string += '\n'
                string = string.rstrip()
                return string

    def __repr__(self):
        """ canonical str """
        return "Rectangle({}, {})".format(str(self.__width), str(self.__height))

    def __del__(self):
        print("Bye rectangle...")
