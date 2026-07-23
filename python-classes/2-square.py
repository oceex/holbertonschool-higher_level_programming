#!/usr/bin/python3
""" setting size """


class Square:
    """ square with a private value """
    def __init__(self, size=0):
        """ setting size value """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
