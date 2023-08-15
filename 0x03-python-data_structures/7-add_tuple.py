#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """add first two numbers of two tuple"""

    if tuple_a is None:
        return tuple(list(tuple_b[:2]))
    elif tuple_b is None:
        return tuple(list(tuple_a[:2]))

    # add two zeros at the end of the tuple
    # if the tuple is empty will be the first
    # else i need first two numbers only
    tuple_A = list(tuple_a)[:]
    tuple_A.extend([0, 0])

    tuple_B = list(tuple_b)[:]
    tuple_B.extend([0, 0])

    new_tuple = [tuple_A[0] + tuple_B[0], tuple_A[1] + tuple_B[1]]

    return tuple(new_tuple)
