#!/usr/bin/python3
element_at = __import__('1-element_at').element_at


def delete_at(my_list=[], idx=0):
    if element_at(my_list, idx):
        my_list.remove(my_list[idx])
    return my_listy
