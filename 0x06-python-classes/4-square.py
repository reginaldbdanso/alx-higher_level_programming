#!/usr/bin/python3

"""This module defines the Square class."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        """Initialize the Square object.

         Args:
            size - size of the square
            defaults to 0 if nothing is passed.
            Must be an integer not less than 0."""

        self.__size = size

    def area(self):
        """Calculates and returns the area of a square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves private instance attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets private instance attribute.

         Raises:
            TypeError - when size passed is not an integer.
            ValueError - when size is less than 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
