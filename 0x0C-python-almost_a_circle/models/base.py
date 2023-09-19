#!/usr/bin/python3
"""representing the Base Class"""


class Base:
    """
    Base Class of other other classes in the module

    attributes:
        __nb_object (int): instances number from this class
    """

    __nb_object = 0

    def __init__(self, id=None):
        """
        initialization (constructor) method

        Args:
            id (int | None): the id of the instance, if it is None
            the id will be with its instance number (Base.__nb_object)
            otherwise will be the value
        """
        if id is None:
            Base.__nb_object += 1
            self.id = Base.__nb_object
        elif isinstance(id, int):
            self.id = id
