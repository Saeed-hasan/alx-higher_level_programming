#!/usr/bin/python3

"""
Moudle-1: Mylist

inhirts from a list,
contain public method that sort list
"""


class MyList(list):
    """ inherts from a list"""

    def __init__(self):
        """ initializes the object """
        super().__init__()

    def print_sorted(self):
        """ print the the list but sorted """
        sorted_list = sorted(self)
        print(sorted_list)
