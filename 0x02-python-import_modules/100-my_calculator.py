#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def basic_calc(expersion):
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if len(expersion) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif expersion[1] not in ops.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        a = int(expersion[0])
        b = int(expersion[2])
        op = expersion[1]
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, ops[op](a, b)))


if __name__ == "__main__":
    basic_calc(argv[1:])
