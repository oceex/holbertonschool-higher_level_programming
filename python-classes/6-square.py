#!/usr/bin/python3
""" bet SQUARE version erer """


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ intioalazing new Suqare """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ returinging Square size """
        return self.__size

    @property
    def position(self):
        """ returning Square position """
        return self.__position

    @size.setter
    def size(self, size):
        """ setting Square size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @position.setter
    def position(self, value):
        """ setting Square position """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ calculating the area """
        return self.__size * self.__size

    def my_print(self):
        """ printing the Square """
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end="")
            for n in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
