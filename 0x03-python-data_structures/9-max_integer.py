#!/usr/bin/python3
""" MAX -> INT """


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    max = my_list[0]

    for qq in my_list:
        if qq > max:
            max = qq
    return max
