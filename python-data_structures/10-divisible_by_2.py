#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    k = []
    for n in my_list:
        k.append(n % 2 == 0)
    return k
