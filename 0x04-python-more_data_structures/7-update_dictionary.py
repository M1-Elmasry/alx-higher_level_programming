#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return None
    elif key is None:
        return a_dictionary
    else:
        new_dict = a_dictionary
        new_dict[key] = value
        return new_dict
