#!/usr/bin/python3
"""
Moudle: 2_square
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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
