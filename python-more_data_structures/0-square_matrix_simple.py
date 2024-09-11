#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    i , j = 0, 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix.append(matrix[i][j] ** 2)

    return new_matrix