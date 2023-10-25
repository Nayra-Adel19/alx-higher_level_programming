#!/usr/bin/python3
""" PYTHON """


def fizzbuzz():

    for qq in range(1, 101):
        if ((qq % 3 == 0) and (qq % 5 == 0)):
            print('FizzBuzz', end=' ')
        elif (qq % 3 == 0):
            print('Fizz', end=' ')
        elif (qq % 5 == 0):
            print('Buzz', end=' ')
        else:
            print('{:d} '.format(qq), end='')
