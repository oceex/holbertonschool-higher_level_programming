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

    def to_json(self):
        " JSON "
        return self.__dict__
