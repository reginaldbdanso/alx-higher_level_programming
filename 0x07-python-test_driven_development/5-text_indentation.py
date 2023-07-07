#!/usr/bin/python3

"""This module defines the Square class."""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    lines = text.splitlines()

    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace
        if line:  # Skip empty lines
            for char in line:
                print(char, end='')
                if char in punctuations:
                    print('\n\n', end='')
            print()
