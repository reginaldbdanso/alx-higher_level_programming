#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # for i in matrix:
    #     for j in matrix[i]:
    #         j = j**2
    return [[j**2 for j in i] for i in matrix]
