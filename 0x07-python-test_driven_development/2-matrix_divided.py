#!/usr/bin/python3

"""This is the matrix_divided module."""


def matrix_divided(matrix, div):
    """divides all elements of a matrix."""
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    num_rows = len(matrix)
    if num_rows == 0:
        raise TypeError("matrix must not be empty")
    
    num_cols = len(matrix[0])
    for row in matrix:
        if len(row) != num_cols:
            raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(element / div, 2))
        result.append(new_row)
    
    return result
