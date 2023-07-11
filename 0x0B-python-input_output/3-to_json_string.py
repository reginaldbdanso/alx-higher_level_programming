#!/usr/bin/python3
"""
module validates whether an object is an instance
of, or is an instance of a class inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class:
        checks if obj is the same insatance as class
        or of the parent class

    Args:
        obj - passed object to be checked
        a_class - passed class to be compared

    Return:
        True if the object is exactly as class
        otherwise, False.
    """
    if isinstance(obj, a_class):
        return True

    else:
        return False
