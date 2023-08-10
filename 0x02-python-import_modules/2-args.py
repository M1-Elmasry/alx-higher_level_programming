#!/usr/bin/python3
from sys import argv


def print_args(args):
    n_args = len(args)
    if n_args > 2:
        print("{:d} arguments:".format(n_args - 1))
        for n in range(1, n_args):
            print("{:d}: {:s}".format(n, argv[n]))

    elif n_args == 2:
         print("1 argument:")

    else:
        print("0 arguments.")


if __name__ == "__main__":
    print_args(argv)
