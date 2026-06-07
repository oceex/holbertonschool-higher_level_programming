#!/usr/bin/python3
element_at = __import__('1-element_at').element_at


def replace_in_list(my_list, idx, element):
    if element_at(my_list, idx):
        my_list[idx] = element
    return my_list
