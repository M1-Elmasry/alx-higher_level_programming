#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if my_list is None:
        return None

    my_list = my_list[:idx] + my_list[idx + 1:]
    return my_list
