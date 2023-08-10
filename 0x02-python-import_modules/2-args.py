#!/usr/bin/python3
from sys import argv


def print_args(args):
    n_args = len(args)
    if n_args > 1:
        print("{:d} argument{:s}".format(n_args - 1, ":" if n_args == 2 else "s:"))
        for n in range(1, n_args):
            print("{:d}: {:s}".format(n, argv[n]))
    else:
        print("0 arguments.")


if __name__ == "__main__":
    print_args(argv)
