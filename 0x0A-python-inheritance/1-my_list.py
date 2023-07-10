#!/usr/bin/python3
"""
MyList module
"""


class MyList(list):
    """
    MyList child class inherits from the
    list base class
    """

    def print_sorted(self):
        """prints list in a sorted order"""
        print(sorted(self))
