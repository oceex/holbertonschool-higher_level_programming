#!/usr/bin/python3


def max_integer(my_list=[]):
    if not len(my_list):
        return None
    n = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > n:
            n = my_list[i]
    return n
