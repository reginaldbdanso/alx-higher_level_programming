#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == [[]]:
        print()
    else:
        new_matrix = matrix.copy()
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[i])):
                # if j == len(matrix[i]) - 1:
                #     print('{:d}'.format(new_matrix[i][j]))
                # else:
                # print('{:d} '.format(new_matrix[i][j]), end='')
                new_matrix[i][j] **= 2
    return new_matrix
