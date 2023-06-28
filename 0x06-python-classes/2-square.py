#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initialize an instance of a square

        Args:
            size - size of the square
            and defaults to 0 if nothing is passed.
            Must be an integer not less than 0.

        Raises:
            TypeError - when size passed is not an integer.
            ValueError - when size is less than 0."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
