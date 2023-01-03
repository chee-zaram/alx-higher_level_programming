#!/usr/bin/python3
"""``101-locked_class`` module

Contains the lone class ``LockedClass``"""


class LockedClass:
    """Prevents the user from dynamically creating a new instance attribute

    Only instance variable permitted is `first_name`
    """

    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        self.first_name = first_name
