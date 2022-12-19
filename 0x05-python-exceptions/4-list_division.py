#!/usr/bin/python3

def list_division(my_list, my_list_2, list_length):
    """Function that divides an element in my_list by the element at the
    corresponding index in my_list_2
    """

    ret_list = []
    for list_len_ret in range(list_length):
        try:
            res = 0
            res = my_list[list_len_ret] / my_list_2[list_len_ret]
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            ret_list.append(res)
    return ret_list
