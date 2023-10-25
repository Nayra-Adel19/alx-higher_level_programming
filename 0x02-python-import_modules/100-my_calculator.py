#!/usr/bin/python3
""" PYTHON """
if __name__ == "__main__":

    import sys

    from sys import exit

    from calculator_1 import add, sub, mul, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    qq = sys.argv[2]
    operator = {"+": add, "-": sub, "*": mul, "/": div}

    if qq not in list(operator.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, qq, b, operator[qq](a, b)))
