#!/usr/bin/python3
"""
in
"""


def inherits_from(obj, a_class):
    " inherits "
    return obj.__class__ != a_class and issubclass(obj.__class__, a_class)
