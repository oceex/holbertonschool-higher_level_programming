#!/usr/bin/python3
""" bset SQUARE version erer """


class Square:
    """ Square class """
    def __init__(self, size=0):
        """ intioalazing new Suqare """
        self.size = size

    @property
    def size(self):
        """ returinging Square size """
        return self.__size

    @size.setter
    def size(self, size):
        """ setting Square size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ calculating the area """
        return self.__size * self.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __eq__(self, other):
        return self.__size == other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __gt__(self, other):
        return self.__size > other.__size
