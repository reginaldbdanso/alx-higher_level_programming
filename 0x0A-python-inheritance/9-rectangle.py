#!/usr/bin/python3
"""the rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines a rectangle class"""
    def __init__(self, width, height):
        """constructor for a rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """
        returns a string representation
        of the rectangle object
        """
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
