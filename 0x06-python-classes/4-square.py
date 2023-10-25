#!/usr/bin/python3
""" Sqhhhuare """


class Square:
    """ ShhhSSquare """

    def __init__(self, size=0):
        """ IgggIInit """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ AAAreaghghh """
        return self.__size ** 2

    @property
    def size(self):
        """ SSSizgggge """
        return self.__size

    @size.setter
    def size(self, value):
        """ SSghgggSize """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
