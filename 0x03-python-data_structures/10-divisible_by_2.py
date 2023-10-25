#!/usr/bin/python3
""" PYTHON """


def divisible_by_2(my_list=[]):
    is_list_divisible_by_2 = []

    for qq in my_list:
        if qq % 2 == 0:
            is_list_divisible_by_2.append(True)

        else:
            is_list_divisible_by_2.append(False)

    return is_list_divisible_by_2
