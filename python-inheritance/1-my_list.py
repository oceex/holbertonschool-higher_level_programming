#!/usr/bin/python3
"""
adding print sorted list
"""


class Mylist(list):
    " sorting "
    def print_sorted(self):
        " wow "
        m = sorted(self)
        print(m)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
