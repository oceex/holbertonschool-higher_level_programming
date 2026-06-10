#!/usr/bin/python3


def uniq_add(my_list=[]):
    m = 0
    for n in my_list:
        if my_list.count(n) == 1:
            m += n
    return m
