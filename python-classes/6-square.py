#!/usr/bin/python3
""" bet SQUARE version erer """


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
    def position(self, s):
        """ setting Square position """
        if isinstance(s, tuple):
            if len(s) == 2:
                if isinstance((s[0], s[1]), int) and s[0] > 0 and s[1] > 0:
                    self.__position = s
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
                print(' ' * self.__position[0], end="")
                for m in range(self.__size):
                    print('#', end="")
                print()
