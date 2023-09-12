#!/usr/bin/python3
"""a module represnts myInt class"""


class MyInt(int):
    """myInt class"""

    def __eq__(self, other):
        if isinstance(other, int):
            return int(self) != int(other)
        return False

    def __ne__(self, other):
        if isinstance(other, int):
            return int(self) == int(other)
        return False
