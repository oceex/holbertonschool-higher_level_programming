#!/usr/bin/python3


def weight_average(my_list=[]):
    result = 0
    for i in range(len(my_list)):
        mul = 1
        for j in range(len(my_list[i])):
            mul *= my_list[i][j]
        result += mul
    return result/len(my_list)
