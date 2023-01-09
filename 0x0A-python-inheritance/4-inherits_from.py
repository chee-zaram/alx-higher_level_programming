#!/usr/bin/python3
"""Module for a function
"""


def inherits_from(obj, a_class):
    """Say if `obj` is an instance of a class that inherits from a_class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
