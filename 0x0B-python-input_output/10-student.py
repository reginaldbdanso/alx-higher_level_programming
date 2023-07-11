#!/usr/bin/python3
"""the square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square class"""
    def __init__(self, size):
        """constructor for sqaure instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of the square"""
        return self.__size ** 2
