#!/usr/bin/python3

"""This module defines the Square class."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square object.

         Args:
            size - size of the square
            defaults to 0 if nothing is passed.
            Must be an integer not less than 0.

            position - coordinates
            defaults to (0, 0) if nothing is passed.
            Must be a tuple of 2 positive integers.
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple)) or \
                (position[0] < 0) or (position[1] < 0) or \
                (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates and returns the area of a square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with character #"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for l in range(self.__position[1]):
                    print()
            elif self.__position[1] == 0:
                pass
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(' ', end='')
                for k in range(self.__size):
                    print('#', end='')
                print()

    @property
    def size(self):
        """Retrieves private instance attribute."""
        return self.__size

    @property
    def position(self):
        """Retrieves private instance attribute"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """Sets private instance attribute.

        Raises:
            TypeError - when position isn't a tuple of 2 positive integers.
            """
        if (not isinstance(value, tuple)) or (value[0] < 0) or \
                (value[1] < 0) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = value
