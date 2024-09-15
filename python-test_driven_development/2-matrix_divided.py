#!/usr/bin/python3

"""Define a matrix division function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix
    matrix must be a list of lists of integers or floats
    Raises:
        TypeError: if matrix must be a matrix (list of lists) of integers/float
        TypeError: if Each row of the matrix must have the same size
        TypeError: if div must be a number
        ZeroDivisionError: if division by zero
    """

    new_matrix = []
    i, j = 0, 0

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    str = "matrix must be a matrix (list of lists) of integers/floats"
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(str)

    str = "Each row of the matrix must have the same size"
    for i in range(len(matrix) - 1):
        for j in range(len(matrix)):
            if len(matrix[i]) != len(matrix[j]):
                raise ValueError(str)

    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
                new_row.append(round(matrix[i][j] / div, 2))


        new_matrix.append(new_row)
    return new_matrix
