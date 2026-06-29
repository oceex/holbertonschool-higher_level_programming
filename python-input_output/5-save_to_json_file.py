#!/usr/bin/python3
"""
kk kk k
"""

import json


def save_to_json_file(my_obj, filename):
    " reall jsooonn "
    with open(filename, "w") as x:
        json.dump(my_obj, x)
