#!/usr/bin/python3
"""This module contains a function to find peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Returns peak value in the list of integers specified by `list_of_integers`
    """

    if not list_of_integers or type(list_of_integers) != list:
        return

    if not all(type(integer) == int for integer in list_of_integers):
        raise TypeError("list_of_integers must be a list of integers")

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]

    if n == 2:
        return max(list_of_integers)

    mid = n // 2

    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    return list_of_integers[mid]
