#!/usr/bin/python3
def islower(c):
    if type(c) is not chr:
        raise TypeError("s must be a char")
    return c >= 'a' and c <= 'z'
