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

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter width """
        self.__width = width

    @property
    def height(self):
        """ getter heigth """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter height """
        self.__height = height

    @property
    def x(self):
        """ getter x """
        return self.__x

    @x.setter
    def x(self, x):
        """ setter x"""
        self.__x = x

    @property
    def y(self):
        """ getter y """
        return self.__y

    @y.setter
    def y(self, y):
        """ setter y """
        self.__y = y
