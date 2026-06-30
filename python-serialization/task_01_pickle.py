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
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        " kk k k piiicklle "
        with open(filename, "w") as x:
            pickle.dump(self.__dict__, x)

    @classmethod
    def deserialize(cls, filename):
        " kk k kk k de pickle "
        try:
            with open(filename, "r") as x:
               return pickle.load(x)
        except Eception:
            return None
