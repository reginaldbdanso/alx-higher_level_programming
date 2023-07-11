#!/usr/bin/python3
"""
json module imported
The load_from_json_file module
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file funcion
    returns an object (Python data structure)
    represented by a JSON string

    Args:
        @filename: filename or path
    """

    with open(filename, "r") as file:
        json_str = file.read()
        obj = json.loads(json_str)
        return obj
