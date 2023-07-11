#!/usr/bin/python3
"""The read_file module"""


def read_file(filename=""):
    """read_file funcion definition"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
