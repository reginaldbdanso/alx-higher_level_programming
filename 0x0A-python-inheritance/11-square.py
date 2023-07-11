#!/usr/bin/python3
"""the Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square class"""
    def __init__(self, size):
        """constructor for the size instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """
        returns the string representation
        of the square object
        """
        return f"[{type(self).__name__}] {self.__size}/{self.__size}"
