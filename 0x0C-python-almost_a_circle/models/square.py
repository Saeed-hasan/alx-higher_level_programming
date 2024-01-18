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

    def update(self, *args, **kwargs):
        """ update square by new value """
        if args is not None and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        else kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
