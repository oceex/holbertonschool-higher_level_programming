#!/usr/bin/python3
"""
isn't?
"""


def is_same_class(obj, a_class):
    " are we? "
    if type(obj) == bool and a_class == int:
        return False
    if type(obj) == int and a_class == bool:
        return False
    if type(obj) == bool and a_class == bool:
        return True
    if type(obj) == int and a_class == int:
        return True
    if type(obj) == list and a_class == list:
        return True
    return isinstance(obj, type(a_class))
