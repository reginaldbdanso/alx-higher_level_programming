#!/usr/bin/python3
"""
json module imported
The save_to_json_file module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file funcion
    returns an object (Python data structure)
    represented by a JSON string

    Args:
        @my_obj: object to be converted
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
    