#!/usr/bin/python3
"""
representing a class that inherits from list
and add some features
"""


class MyList(list):
    """a child class from list"""

    def __init__(self):
        """init the object"""
        super().__init__()

    def print_sorted(self):
        """print list in ascending order"""
        return print(sorted(self))
