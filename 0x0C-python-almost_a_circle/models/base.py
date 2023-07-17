#!/usr/bin/python3
"""
This is the base class from which
all other classes will inherit
"""


class Base:
    """
    Base class definition
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor for the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
