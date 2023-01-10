#!/usr/bin/python3
"""Module ``0-read_file``"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints to stdout

    Args:
        filename (str): Filename to read from as a string

    Return:
        None if no file is passed or None is passed or `filename` is not passed
    """

    if not filename:
        return
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
