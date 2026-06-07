#!/usr/bin/python3


def no_c(my_string):
    new = ""
    for c in my_string:
        if not c == "c" and not c == "C":
            new += c
    return new
