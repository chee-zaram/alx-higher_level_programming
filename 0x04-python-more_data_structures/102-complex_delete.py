#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Function that deletes all keys with a specific value in a dictionary.
    """

    if a_dictionary:
        del_list = []
        for k, v in a_dictionary.items():
            if v is value:
                del_list.append(k)
        for item in del_list:
            del a_dictionary[item]

        return a_dictionary
