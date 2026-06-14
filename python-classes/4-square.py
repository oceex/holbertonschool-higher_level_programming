#!/usr/bin/python3
""" Square class """


class Square:
    """ the best square """
    def __init__(self, size=0):
        """ initialzing square """
        size(size)

    def size(self):
        """ returning size """
        return self.__size

    def size(self, size):
        """ setting size """
        if not isinstance(size, int):
            raise TypeError("")
        elif size < 0:
            raise ValueError("")
        else:
            self.__size = size

    def area(self):
        """ calculating the area """
        return size * size
