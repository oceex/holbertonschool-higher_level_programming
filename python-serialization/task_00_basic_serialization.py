#!/usr/bin/python3
"""
kk kkk k k k k kk
"""


import json


def serialize_and_save_to_file(data, filename):
    " saving to a json "
    with open(filename, "w") as x:
        json.dump(data, x)


def load_and_deserialize(filename):
    " loading from a json "
    with open(filename, "r") as x:
        return json.load(x)
