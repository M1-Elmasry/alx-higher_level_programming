#!/usr/bin/python3
"""representing a from_json_string function"""

json_loads = __import__("json").loads


def from_json_string(my_obj):
    """
    returns an object (Python data structure)
    represented by a JSON string
    """
    return json_loads(my_obj)
