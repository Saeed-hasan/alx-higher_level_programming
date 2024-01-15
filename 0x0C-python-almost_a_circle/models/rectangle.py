#!/usr/bin/python3
"""module rectangle"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """
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
    def width(self, value):
        """ settter width """
        return self.__width = value

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ settter height """
        return self.__height = value

    @property
    def x(self):
        """ getter x """
        return self.__x

    @x.setter
    def x(self, value):
        """ settter x """
        return self.__x = value

    @property
    def y(self):
        """ getter y """
        return self.__y

    @y.setter
    def y(self, value):
        """ settter y """
        return self.__y = value
