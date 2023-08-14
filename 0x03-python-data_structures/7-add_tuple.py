#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a, len_b = len(tuple_a), len(tuple_b)

    if tuple_a is None or len_a == 0:
        return tuple_b
    elif tuple_b is None or len_b == 0:
        return tuple_a

    new_tuple = [0, 0]
    new_tuple[0] = tuple_a[0] + tuple_b[0]

    if len_a == 1:
        new_tuple[1] = tuple_b[1]
    elif len_b == 1:
        new_tuple[1] = tuple_a[1]
    else:
        new_tuple[1] = tuple_b[1] + tuple_a[1]

    return tuple(new_tuple)
