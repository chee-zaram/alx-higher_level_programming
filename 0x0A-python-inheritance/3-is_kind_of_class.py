#!/usr/bin/python3
"""This is the ``3-is_kind_of_class.py``

Contains the long function ``is_kind_of_class``"""


def is_kind_of_class(obj, a_class):
    """Tells whether `obj` is an instance of `a_class` or any of its subclasses

    Args:
        obj: Object to check
        a_class: Class to check agains

    Return:
        True if the object is an instance of any of them
        False otherwise
    """
    return isinstance(obj, a_class)
