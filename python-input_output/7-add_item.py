#!/usr/bin/python3
"""
k kkk k k k k kkk k k kk k
"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
import json
import sys
import os


def main():
    " maimai "
    x = []
    if os.path.exists("add_item.json") and os.path.getsize("add_item.json"):
        x = list(load_from_json_file("add_item.json"))
    for n in sys.argv[1:]:
        x.append(n)
    save_to_json_file(x, "add_item.json")


if __name__ == "__main__":
    main()
