#!/usr/bin/python3
from sys import argv


def print_args():
    n_args = len(argv)
    if n_args > 1:
        print("{:d} arguments:".format(n_args - 1))
        for n in range(1, n_args):
            print("{:d}: {:s}".format(n, argv[n]))
    else:
        print("0 arguments.")


if __name__ == "__main__":
    print_args()
