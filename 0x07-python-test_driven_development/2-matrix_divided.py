#!/usr/bin/python3
""" module that divides all elements of a matrix of similar sized rows """


def matrix_divided(matrix, div):
    """ function that returns a new matrix with each element divided by da div

    Args:
        matrix: a 2d array, each row should be the same size or else: error
        div: a number that is not 0 or else error

    Returns: a new matrix with each element adjusted to the div amount
    """
    errmessage = "matrix must be a matrix (list of lists) of integers/floats"
    new = []
    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(errmessage)
    if type(div) is int or type(div) is float or div is None:
        pass  # improper div value type checks
    else:
        raise TypeError("div must be a number")
    if div == 0:  # if div is zero
        raise ZeroDivisionError("division by zero")
    if matrix[0]:  # if matrix is empty or not
        length = len(matrix[0])
    else:
        raise TypeError(errmessage)
    for i in range(len(matrix)):  # real work. the appending
        if len(matrix[i]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        new.append([])
        for t in matrix[i]:
            if type(t) is int or type(t) is float:
                new[i].append(round(t / div, 2))
            else:
                raise TypeError(errmessage)
    return new
