#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None:
        return None

    max = my_list[0] if len(my_list) >= 1 else None
    for n in my_list:
        if n > max:
            max = n

    return max
