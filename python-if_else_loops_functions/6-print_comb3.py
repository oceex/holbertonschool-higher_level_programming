#!/usr/bin/python3
n = 9
m = 0
while n:
    for i in range(n):
        if i == n - 1 and n == 1:
            print("{}{}".format(m, m + 1 + i))
        else:
            print("{}{}, ".format(m, m + 1 + i), end="")
    n -= 1
    m += 1
