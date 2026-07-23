#!/usr/bin/python3
""" Square class """


class Square:
    """ the best square """
    def __init__(self, size=0):
        """ initialzing square """
        self.__size = size

    @property
    def size(self):
        """ returning size """
        return self.__size

    @size.setter
    def size(self, size):
        """ setting size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ calculating the area """
        return (self.__size) * (self.__size)
