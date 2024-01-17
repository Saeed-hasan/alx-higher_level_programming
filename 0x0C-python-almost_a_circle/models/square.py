#!/usr/bin/python3
'''
    Class square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
        Defining the square class
        Inherits from:
            rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size (int): The length of each side of the square.
            x (int): The x-coordinate of the square's position (default 0).
            y (int): The y-coordinate of the square's position (default 0).
            id (int): The ID of an instance of this class (default None).
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return class representation """
        txt = '[Square] ({}) {}/{} - {}'
        txt = txt.format(self.id, self.x, self.y, self.size)
        return txt

    @property
    def size(self):
        """ getter """
        return self.height
        return self.width

    @size.setter
    def size(self, value):
        """ setter """
        self.width = value
        self.height = value
