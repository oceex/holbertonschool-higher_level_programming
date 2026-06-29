#!/usr/bin/python3
"""
k kkk k k kk
"""


def pascal_triangle(n):
    " pascall "
    x = []
    if n <= 0:
        return x
    for m in range(n):
        v = [1 for b in range(m+1)]
        x.append(v)
    for i in range(len(x)):
        for j in range(len(x[i])):
            if j == 0 or i == j:
                x[i][j] = 1
            else:
               x[i][j] = x[i-1][j] + x[i-1][j-1]
    return x
