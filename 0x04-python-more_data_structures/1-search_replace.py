#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Function to replace an item in a list with another.

    Parameters:
        my_list: List to search for item in.
        search: Item to replace.
        replace: Item to replace with.

    Return:
        A new list with the new item.
    """

    new_list = my_list.copy()
    for idx in range(len(my_list)):
        if new_list[idx] is search:
            new_list.pop(idx)
            new_list.insert(idx, replace)

    return new_list
