#!/usr/bin/python3
"""
k k kkk kk kk
"""


def append_after(filename="", search_string="", new_string=""):
    " k kkk k k k "
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if new_string in line:
                f.write(new_string)xy
