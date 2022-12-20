#!/usr/bin/python3
"""A module that has definition of a class Square"""


class Square:
    """This a class containing a private instance attribute `__size`

    Instantiation with `size` is optional.
    """

    def __init__(self, size=0):
        """Initializes the attribute"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
