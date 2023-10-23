#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    aa = 0
    for ss in range(x):
        try:
            print("{:d}".format(my_list[ss]), end="")
            aa = aa + 1

        except (ValueError, TypeError):
            continue
    print()
    return aa
