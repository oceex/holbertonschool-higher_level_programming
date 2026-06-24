#!/usr/bin/pyhton3
"""
k
k
"""


class CountedIterator:
    " k k "
    def __init__(self, item):
        " k k "
        self.__count = 0
        self.__data = item

    def __iter__(self):
        " k k "
        self.__count = 0
        return self

    def __next__(self):
        " k k "
        if self.__count >= len(self.__data):
            raise StopIteration
        v = self.__data[self.__count]
        self.__count += 1
        return v

    def __len__(self):
        return len(self.__data)

    def get_count(self):
        " k k "
        return self.__count
