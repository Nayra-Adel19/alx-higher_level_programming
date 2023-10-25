#!/usr/bin/python3
""" PRINT MATRIXI """


def print_matrix_integer(matrix=[[]]):

    for qq in matrix:
        for aa in qq:
            print("{:d}".format(aa), end=" " if aa != qq[-1] else "")
        print()
