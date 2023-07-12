#!/usr/bin/python3
"""
a class Student that defines a student
"""


class Student:
    """
    This is the student class
    """

    def __init__(self, first_name, last_name, age):
        """
        The init constructor
        Args:
            @self: instance
            @first_name: first name string
            @last_name: last name string
            @age: age string
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        The to_json function
        Args:
            @self: instance.
        """

        json_obj = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return json_obj
