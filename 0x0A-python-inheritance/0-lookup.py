#!/usr/bin/python3
"""This is the ``0-lookup`` module

It contains the lone function ``lookup``"""


def lookup(obj):
    """Function that returns a list of available attributes and methods of obj
    """
    return dir(obj)
