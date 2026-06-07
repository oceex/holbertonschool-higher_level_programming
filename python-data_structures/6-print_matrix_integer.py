#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    m, n = len(matrix), len(len(matrix))
    for i in range (m):
        for j in range (n):
            if not j == n - 1:
                print("{:d}"format.(matrix[i][j]), end=" ")
            else:
                print("{:d}"format.(matrix[i][j]))
