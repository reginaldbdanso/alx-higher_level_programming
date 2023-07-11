#!/usr/bin/python3
"""
module validates whether or not an
object is exactly an instance of a class
"""


def is_same_class(obj, a_class):
    """
    is_name_class - checks if obj is the same as class

    Args:
        obj - passed object to be checked
        a_class - passed class to be compared

    Return:
        True if the object is exactly as class
        otherwise, False.
    """
    if type(obj) is a_class:
        return True

    else:
        return False
