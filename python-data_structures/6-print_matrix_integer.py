#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    m, n = len(matrix), 0
    for i in range(m):
        n += len(matrix[i])
        for j in range(len(matrix[i])):
            if not j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]))
    if not n:
        print()
