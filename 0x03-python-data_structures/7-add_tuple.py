#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = [0, 0]
    try:
        new_tuple[0] = tuple_b[0] + tuple_a[0]
        new_tuple[1] = tuple_b[1] + tuple_a[1]
        return tuple(new_tuple)

    except IndexError:
        len_b = len(tuple_b)
        len_a = len(tuple_a)
        if len_b > 0:
            new_tuple[0] += tuple_b[0]
        if len_a > 0:
            new_tuple[0] += tuple_a[0]
        if len_b >= 2:
            new_tuple[1] += tuple_b[1]
        if len_a >= 2:
            new_tuple[1] += tuple_a[1]
        return tuple(new_tuple)
