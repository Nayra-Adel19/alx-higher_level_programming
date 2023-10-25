#!/usr/bin/python3
""" PYTHON """


def print_last_digit(number):
    """ PYTHON """

    if number < 0:
        number = -1 * number

    print(number % 10, end="")

    return number % 10
