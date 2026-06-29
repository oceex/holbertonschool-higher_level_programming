#!/usr/bin/python3
"""
k kkk k k k k kkk k k kk k
"""

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
import json, sys

x = load_from_json_file("add_item.json")

for n in sys.args:
    x.append(n)

save_to_json_file(x, "add_item.json")


