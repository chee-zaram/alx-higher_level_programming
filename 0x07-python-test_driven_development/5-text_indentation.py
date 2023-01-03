#!/usr/bin/python3
"""This is the ``5-text_indentation`` module

It contains the function ``text_indentation``
"""


def text_indentation(text):
    """Prints a text with 2 new lines in place of characters in ['.', '?', ':']

    Args:
        text (str): The text to be indented

    Raises:
        TypeError: If `text` is not a string

    Example:
    >>> text_indentation("One time for the real ones. Are they really real?")
    One time for the real ones.
    <BLANKLINE>
    Are they really real?
    <BLANKLINE>
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # loop through for each special_char and replace with newlines
    for special_char in ('.', '?', ':'):
        text = (special_char + ('\n' * 2)).join(
                [line.lstrip(' ') for line in text.split(special_char)]
                )

    # print newly formed string
    print("{}".format(text), end='')
