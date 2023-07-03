#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """This the Rectangle class."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object.

         Args:
            width - width of the rectangle
            height - height of the rectangle
            defaults to 0 if nothing is passed.
            Must be an integer not less than 0."""
        Rectangle.number_of_instances += 1
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

    def area(self):
        """returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width + self.__width + self.__height + self.__height

    def __str__(self):
        """returns the string rep of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        stringB = ""
        for i in range(self.__height):
            for j in range(self.__width):
                stringB += str(self.print_symbol)
            stringB += '\n'
        return stringB[:-1]

    def __repr__(self):
        """returns the string rep of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints instance deletion message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
    @classmethod
    def square(cls, size=0):
        """returns a new rectangle instance"""
        return cls(size, size)
