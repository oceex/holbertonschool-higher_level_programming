#!/usr/bin/python3
"""
adding print sorted list
"""


class MyList(list):
    " sorting listss "
    def print_sorted(self):
        " wow is woww "
        m = sorted(self)
        return m


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
