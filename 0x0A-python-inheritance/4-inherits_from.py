#!/usr/bin/python3
"""
    module validates if the instance of an object of a class
    is inherited directly or indirectly from a specified class
"""


def inherits_from(obj, a_class):
    """
    inherits_from:
        checks if object is the same instance of an
        object of a class is inherited directly
        or not

    Args:
        obj: passed object to be checked
        a_class: passed class to be compared

    Return:
        True if the type of object is a subclass of
        a class. Otherwise, False.
    """
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    else:
        return False
