#!/usr/bin/python3

def simple_delete(a_dcitionary, key=""):
    if a_dcitionary is None:
        return None

    if key in a_dcitionary.keys():
        del a_dcitionary[key]

    return a_dcitionary
