#!/usr/bin/python3
"""
Created on Tue May 25 2020
@author: saeed
"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
