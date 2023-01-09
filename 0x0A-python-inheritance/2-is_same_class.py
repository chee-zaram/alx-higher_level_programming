#!/usr/bin/python3
"""This is the ``2-is_same_class`` module

It contains the ``is_same_class`` function
"""


def is_same_class(obj, a_class):
    """Says whether `obj` is exactly an instance of `a_class`

    Args:
        obj: The object to check
        a_class: A class to check if `obj` is an instance of

    Return:
        True if `obj` is an instance of `a_class`
        False otherwise
    """
    return type(obj) is a_class
