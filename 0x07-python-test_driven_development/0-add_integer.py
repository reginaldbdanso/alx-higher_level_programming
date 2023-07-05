#!/usr/bin/python3
"""This is the add_integer module."""


def add_integer(a, b=98):
    """Adds 2 integers"""
    if not isinstance([a, b], [int, float]):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
