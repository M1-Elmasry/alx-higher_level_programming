#!/usr/bin/python3
"""representing a to_json_string function"""

json_dumps = __import__("json").dumps


def to_json_string(my_obj):
    """returns the JSON representation of the @my_obj"""
    return json_dumps(my_obj)
