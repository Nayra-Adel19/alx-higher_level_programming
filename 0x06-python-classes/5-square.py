#!/usr/bin/python3
""" Sqkkkuare """


class Square:
    """ SnmSSquare """

    def __init__(self, size=0):
        """
            Prggivate
            instmmmance
        """
        self.size = size

    @property
    def size(self):
        """ SSSizejjj """
        return self.__size

    @size.setter
    def size(self, value):
        """ SSSimmmze """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ AAArea jjj"""
        return self.__size * self.__size

    def my_print(self):
        """ PPPrinkkkt """

        for i in range(self.size):
            print("#" * self.size)

        if self.size == 0:
            print()
