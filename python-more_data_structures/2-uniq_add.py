#!/usr/bin/python3


def uniq_add(my_list=[]):
    m, c = 0, 1
    while c:
        c = 0
        for n in my_list:
            if my_list.count(n) > 1:
                my_list.remove(n)
                c = 1
    for n in my_list:
        m += n
    return m
