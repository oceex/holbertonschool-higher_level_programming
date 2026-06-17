#!/usr/bin/python3
""" bset SQUARE version erer """


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ intioalazing new Suqare """
        self.size = size
        self.position = position

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
        if (not isinstance(value, tuple) or not len(value) == 2 or
                (not all(isinstance(n, int) and n >= 0 for n in value))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ calculating the area """
        return self.__size * self.__size

    def my_print(self):
        """ printing the Square """
        if not self.__size == 0:
            print('\n' * self.__position[1], end="")
            for n in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
        else:
            print()

    def __str__(self):
        """ printing the Square """
        m = ""
        if not self.__size == 0:
            m += '\n' * self.__position[1]
            for n in range(self.__size):
                m += (' ' * self.__position[0] + '#' * self.__size + '\n')
        else:
            m += '\n'
        return m
