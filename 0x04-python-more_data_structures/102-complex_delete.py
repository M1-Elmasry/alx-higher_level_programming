#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None

    keys_names = [k for k in a_dictionary.keys() if a_dictionary[k] == value]
    for key in keys_names:
        del a_dictionary[key]

    return a_dictionary
