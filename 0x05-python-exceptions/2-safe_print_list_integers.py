#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print(my_list[i], end="")
                counter += 1

        except IndexError:
            raise

    print()
    return counter
