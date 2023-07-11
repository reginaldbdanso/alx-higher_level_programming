#!/usr/bin/python3
"""The write_file module"""


def write_file(filename="", text=""):
    """write_file funcion definition"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
