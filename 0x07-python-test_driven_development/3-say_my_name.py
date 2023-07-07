#!/usr/bin/python3
"""This is the say_my_name module"""


def say_my_name(first_name, last_name=""):
    """ prints my name"""
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(
            "first_name must be a string or last_name must be a string")
    if last_name:
        print("My name is", first_name, last_name)
    else:
        print("My name is", first_name)
