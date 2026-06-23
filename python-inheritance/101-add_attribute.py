#!/usr/bin/python3
"""
adding attr
"""

def add_attribute(obj, name, value):
    " adding attr "
    if hasattr(obj.__class__, "__slots__"):
        raise TypeError("can't add new attribute")
    obj.name = value
