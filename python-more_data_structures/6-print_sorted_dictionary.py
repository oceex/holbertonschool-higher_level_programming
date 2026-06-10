#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    keys = []
    for n in a_dictionary:
        keys.append(n)
    keys.sort()
    for n in keys:
        print(f"{n}: {a_dictionary.get(n)}")
