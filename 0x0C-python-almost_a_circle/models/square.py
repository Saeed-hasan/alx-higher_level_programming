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
        """ main class """
        super().__init__(x, y, id)
        self.size = size
        self.width = size
        self.height = size

    def __str__(self):
        """Return class representation """
        txt = '[Square] ({}) {}/{} - {}'
        txt = txt.format(self.id, self.x, self.y, self.size)
        return txt
