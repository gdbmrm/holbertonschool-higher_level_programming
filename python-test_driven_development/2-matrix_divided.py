#!/usr/bin/python3

def matrix_divided(matrix, div):
    new_matrix = []
    i, j = 0, 0

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(matrix[i]) != len(matrix):
                raise TypeError("Each row of the matrix must have the same size")


    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            try:
                new_row.append(round(matrix[i][j] / div, 2))
            except ZeroDivisionError:
                print("division by zero")
                return new_matrix
            except TypeError:
                print("div must be a number")
                return new_matrix

        new_matrix.append(new_row)
    return new_matrix
