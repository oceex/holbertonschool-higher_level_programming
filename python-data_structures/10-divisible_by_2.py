#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    k = []
    for i in range(len(my_list)):
        k = my_list[i] % 2 == 0
    return k
