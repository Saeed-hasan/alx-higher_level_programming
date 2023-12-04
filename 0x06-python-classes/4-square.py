#!/usr/bin/python3
"""
Moudle: 4_square
Defination of class square
"""
class Square:
    """
    class defintion
    Args: the size of square
    """
    def __init__(self, size=0):
        """
        Initialize square 
        Attributes: __size of square
        """
        self.__size = size

        @property
        def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return ((self.size)**2
