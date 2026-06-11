#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    c = 1
    while c:
        c = 0
        for n in a_dictionary:
            if a_dictionary[n] == value:
                a_dictionary.pop(n)
                c = 1
                break
    return a_dictionary
