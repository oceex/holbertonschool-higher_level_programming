#!/usr/bin/python3
""" privity """


class Square:
    """ Square size private :| """
    __size = 0


    def __init__(self, size):
        self.__size = size
