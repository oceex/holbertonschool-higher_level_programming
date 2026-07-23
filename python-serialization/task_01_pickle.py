#!/usr/bin/python3
"""
k kk k k k k
"""

import pickle


class CustomObject:
    " kkk kk pickle pickle "
    def __init__(self, name, age, is_student):
        " initoaling "
        self.name = name
        self.is_student = is_student
        self.age = age

    def display(self):
        " printing "
        print(f"Name: {self.name}\nAge: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        " kk k k piiicklle "
        with open(filename, "wb") as x:
            pickle.dump(self.__dict__, x)

    @classmethod
    def deserialize(cls, filename):
        " kk k kk k de pickle "
        try:
            with open(filename, "rb") as x:
                data = pickle.load(x)
                dummy = cls(None, None, None)
                dummy.__dict__.update(data)
                return dummy
        except Exception:
            return None
