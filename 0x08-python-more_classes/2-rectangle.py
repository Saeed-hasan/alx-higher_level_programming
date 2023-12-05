#!/usr/bin/python3
"""
Module: 2_rectangle
Contains class Rectangle empty
"""


class Rectangle():

    """
    Defines empty  class rectangle
    """
    def __init__(self, width=0, height=0):
        """ initializion """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(width) not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(height) not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height = value

    def area(self):
        """
        calculate the area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        calculate the perimeter of rectangle
        """
        if self.__width = 0 or self.__height = 0:
            return (0)
        else:
            return 2 * (self.__height + self.__width)
