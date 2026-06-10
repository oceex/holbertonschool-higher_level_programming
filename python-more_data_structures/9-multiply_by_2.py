#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new = {}
    for n in a_dictionary:
        new[n] = a_dictionary.get(n)*2
    return new
