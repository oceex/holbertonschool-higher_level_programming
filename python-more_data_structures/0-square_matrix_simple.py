#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    mat = [[]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            mat[i].append(matrix[i][j] * matrix[i][j])
