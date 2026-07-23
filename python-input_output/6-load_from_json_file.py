#!/usr/bin/python3
"""
k kkk k k k
"""


import json


def load_from_json_file(filename):
    " json "
    with open(filename, "r") as f:
        return json.load(f)
