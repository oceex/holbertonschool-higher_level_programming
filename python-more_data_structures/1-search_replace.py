#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_one = []
    for n in my_list:
        if n == search:
            new_one.append(replace)
        else:
            new_one.append(n)
    return new_one
