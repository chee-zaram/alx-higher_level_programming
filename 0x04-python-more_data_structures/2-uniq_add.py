#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Returns the sum of all unique occurences of an integer in a 1D list.
    """

    total = sum(set(my_list), 0)
    return total
