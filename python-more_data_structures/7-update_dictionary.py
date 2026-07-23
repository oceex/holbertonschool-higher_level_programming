#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    if not a_dictionary.get(key):
        a_dictionary.update({key: value})
    else:
        a_dictionary[key] = value
    return a_dictionary
