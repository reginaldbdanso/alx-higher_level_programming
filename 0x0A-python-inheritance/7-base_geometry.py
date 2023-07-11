#!/usr/bin/python3
""" a BaseGeometry class"""


class BaseGeometry:
    """defines a base geometry class"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate that value is an int and not less than 0"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
