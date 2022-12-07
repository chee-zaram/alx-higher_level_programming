#!/usr/bin/python3
def best_score(a_dictionary):
    """Function that returns a key with the highest integer value from a dict.
    """

    if a_dictionary and len(a_dictionary.values()) != 0:
        ls, maxi = [], 0
        for k, v in a_dictionary.items():
            if v >= maxi:
                maxi = v
                ls.append(k)
        return ls[-1]
