#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    m = len(matrix)
    if not m:
        print('\n')
        return
    for i in range (m):
        for j in range (len(matrix[i])):
            if not j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]))
