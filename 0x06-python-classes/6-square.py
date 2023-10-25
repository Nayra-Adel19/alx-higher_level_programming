#!/usr/bin/python3
""" Sqddduare """


class Square:
    """ SSSddquare """

    def __init__(self, size=0, position=(0, 0)):
        """ SddSSquare """

        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """ SSSdddize """

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        """ SSSquadddre """

        return self.__position

    @position.setter
    def position(self, value):
        """ SSSqudare """

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')

        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """ AAArddea """

        return self.__size ** 2

    def pos_print(self):
        """ Print PdddPPosition """

        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """ PPPriddnt """

        print(self.pos_print(), end='')
