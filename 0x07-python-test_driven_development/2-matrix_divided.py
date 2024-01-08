#!/usr/bin/python3
""" Defines a function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix """
    if type(matrix) is not list:
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err)
    if len(matrix) == 0:
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err)
    for row in matrix:
        if type(row) is not list:
            err = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(err)
        if len(row) == 0:
            err = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(err)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in [int, float]:
                "matrix must be a matrix (list of lists) of integers/floats"
                raise TypeError(err)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
