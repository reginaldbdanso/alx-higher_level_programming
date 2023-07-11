#!/usr/bin/python3
import json
"""
json module imported
The to_json_string module
"""


def to_json_string(my_obj):
    """
    to_json_string funcion
    returns the JSON representation of an object

    Args:
        @my_obj: object to be converted
    """
    return json.dumps(my_obj)
