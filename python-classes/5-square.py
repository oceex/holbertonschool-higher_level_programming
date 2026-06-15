#!/usr/bin/python3
""" square """


class Square:
    """ now printing vesion! """
    def __init__(self, size=0):
        """ initialining """
        self.__size = size

    @property
    def size(self):
        """ get """
        return self.__size

    @size.setter
    def size(self, size):
        """ set """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ finding the area """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for n in range(self.__size):
                for m in range(self.__size):
                    print('#', end="")
                print()
