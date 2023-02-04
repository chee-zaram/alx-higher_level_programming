#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Function that returns the weighted average of all integers tuple of the
    format (<score>, <weight>).
    """

    if my_list:
        sum_of_prods, sum_of_weight = 0, 0
        for score, weight in my_list:
            sum_of_prods += score * weight
            sum_of_weight += weight

        return sum_of_prods / sum_of_weight
    return 0
