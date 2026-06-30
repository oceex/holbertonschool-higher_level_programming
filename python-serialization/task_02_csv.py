#!/usr/bin/python3
"""
k k k k k kkkk
"""


import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as x:
            reader = csv.DictReader(x)
            reader = list(reader)
        with open("data.json", "w") as y:
            json.dump(reader, y)
    except Exception:
        return False
    else:
        return True
