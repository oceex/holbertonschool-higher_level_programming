#!/usr/bin/python3
""" best version """


class Square:
    """ Square and its area """
    def __init__(self, size=0):
        """ setting size up """
        if not isinstance(size, int):
            raise TypeError("")
        elif size < 0:
            raise ValueError("")
        else:
            self.__size = size


    def area(self):
        """ calculate current area """
        return (self.__size) * (self.__size)
