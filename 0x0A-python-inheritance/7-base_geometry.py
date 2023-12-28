#!/usr/bin/python3
"""
Module-7:7-basegeometry
contain two public method
"""


class BaseGeometry:
    """ contain one method """
    def area(self):
        """ impemented aread method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ check validate of integer """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
