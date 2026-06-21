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
    if type == type(a_class):
        return isinstance(obj, a_class)
    return isinstance(obj, type(a_class))
