#!/usr/bin/python3

def simple_delete(a_dcitionary, key=""):
    return {k: v for k, v in a_dcitionary.items() if k != key}
