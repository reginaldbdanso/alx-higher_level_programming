#!/usr/bin/python3
"""
json module imported
The add_item module
"""


def class_to_json(obj):
    """
    add_item - adds all items and saves to a JSON file
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
