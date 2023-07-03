#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """This the Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object.

         Args:
            width - width of the rectangle
            height - height of the rectangle
            defaults to 0 if nothing is passed.
            Must be an integer not less than 0."""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Retrieves private instance attribute."""
        return self.__width

    @property
    def height(self):
        """Retrieves private instance attribute."""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets private instance attribute.

         Raises:
            TypeError - when width passed is not an integer.
            ValueError - when width is less than 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets private instance attribute.

         Raises:
            TypeError - when height passed is not an integer.
            ValueError - when height is less than 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
