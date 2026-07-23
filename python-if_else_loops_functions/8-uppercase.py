#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    for c in str:
        x = ord(c)
        if islower(c):
            x -= 32
        print("{}".format(chr(x)), end="")

    print()
