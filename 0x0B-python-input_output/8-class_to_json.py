#!/usr/bin/python3
"""
module defines a function
that converts a class to JSON
"""


def class_to_json(obj):
    """
    returns a dictionary for json serialization
    Args:
        @obj: object to be converted
    """
    return obj.__dict__
