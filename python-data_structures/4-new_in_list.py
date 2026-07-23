#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list


def new_in_list(my_list, idx, element):
    mine = []
    for n in my_list:
        mine.append(n)
    replace_in_list(mine, idx, element)
    return mine
