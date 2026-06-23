#!/usr/bin/python3
"""
devopling int class
"""


class MyInt(int):
    " more rebel "
    def __eq__(self, other):
        " equaltion "
        return self == other

    def __ne__(self, other):
        " equaltion "
        return self != other

