#!/usr/bin/python3
""" Module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def int_Validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))
        else value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter """
        self.__width = width

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        self.__height = value

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter """
        self.__x = value

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter """
        self.__y = value
