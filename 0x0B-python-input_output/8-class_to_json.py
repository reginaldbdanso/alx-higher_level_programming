#!/usr/bin/python3
"""
json module imported
The class_to_json module
"""


def class_to_json(obj):
    """
    class_to_json - returns the dictionary description
    with simple data structure  for JSON serialization of an object:
    Args:
        @args: arguments that to be added.
        @filename: file to be updated
    """

    if isinstance(obj, (str, int, bool)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    else:
        attributes = {}
        for attr in dir(obj):
            if not attr.startswith("__") and not callable(getattr(obj, attr)):
                attributes[attr] = class_to_json(getattr(obj, attr))
        return attributes
