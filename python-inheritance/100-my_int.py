#!/usr/bin/python3
"""
devopling int class
"""


class MyInt(int):
    " more rebel "
    def __ne__(self, other):
        " equaltion "
        return int(self) == other

    def __eq__(self, other):
        " not equa "
        return int(self) != other

