#!/usr/bin/python3
def islower(c):
    try:
        return c >= 'a' and c <= 'z'
    except ValueError:
        raise TypeError("wrong type")
