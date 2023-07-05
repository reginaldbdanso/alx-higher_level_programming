#!/usr/bin/python3
"""This is the add_integer module."""


def add_integer(a, b=98):
    """Adds 2 integers"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
