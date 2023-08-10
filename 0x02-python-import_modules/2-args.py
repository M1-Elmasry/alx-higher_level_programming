#!/usr/bin/python3
from sys import argv


def print_args():
    n = len(argv)
    if n > 1:
        print("{:d} argument{:s}".format(n - 1, ":" if n == 2 else "s:"))
        for n in range(1, n):
            print("{:d}: {:s}".format(n, argv[n]))
    else:
        print("0 arguments.")


if __name__ == "__main__":
    print_args()
