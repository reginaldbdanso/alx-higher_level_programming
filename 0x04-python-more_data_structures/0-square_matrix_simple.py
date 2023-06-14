#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # List comprehension method

    return [[j**2 for j in i] for i in matrix]
