#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys where all keys are strings.
    """

    if a_dictionary:
        [print("{}: {}".format(k, v)) for k, v in sorted(a_dictionary.items())]
