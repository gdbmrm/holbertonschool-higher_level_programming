#!/usr/bin/python3

def matrix_divided(matrix, div):
    new_matrix = []
    i, j = 0, 0

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
