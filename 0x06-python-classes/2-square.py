#!/usr/bin/python3
""" Da Squjjjare """


class Square:
    """ SSSqummmare """

    def __init__(self, size=0):
        """ Privvcccate instance """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
