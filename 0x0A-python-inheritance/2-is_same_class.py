#!/usr/bin/python3
"""
Moudle-2: is_same class
check exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ check an instace of the class """

    if type(obj) is a_class:
        return True
    else:
        return False
