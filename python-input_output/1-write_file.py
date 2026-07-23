#!/usr/bin/python3
"""
kkk kk
"""


def write_file(filename="", text=""):
    " writng to a very lucky file "
    n = 0
    with open(filename, "w") as x:
        n = x.write(text)
    return n
