#!/usr/bin/python3


def weight_average(my_list=[]):
    if not len(my_list):
        return 0
    result, k = 0, 0
    for i in range(len(my_list)):
        mul = 1
        for j in range(len(my_list[i])):
            mul *= my_list[i][j]
            if j == 1:
                k += my_list[i][j]
        result += mul
    return result/k
