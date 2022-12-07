#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Function to update value of key if present, else create key/value pair.
    """

    a_dictionary[key] = value
    return a_dictionary
