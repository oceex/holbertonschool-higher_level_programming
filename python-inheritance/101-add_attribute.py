#!/usr/bin/python3
"""
adding attr
"""


def add_attribute(obj, name, value):
    " adding attr "
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
