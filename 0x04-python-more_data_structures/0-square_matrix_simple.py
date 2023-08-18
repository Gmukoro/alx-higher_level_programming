#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_trix = matrix.copy()
    for t in range(len(matrix)):
        new_trix[t] = list(map(lambda x: x**2, matrix[t]))
    return x(new_trix)
