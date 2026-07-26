#!/usr/bin/python3
"""
kk kk k k k
"""


class Student:
    " kk k kk "
    def __init__(self, first_name, last_name, age):
        " kk k k kkk k "
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        " JSON "
        if attrs is None or not all(type(x) is str for x in attrs):
            return self.__dict__
        else:
            c = {}
            for a in attrs:
                if a in self.__dict__:
                    c[a] = self.__dict__[a]
            return c

    def reload_from_json(self, json):
        " del every thing!!! "
        if json == {}:
            return
        self.__dict__ = json
