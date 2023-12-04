#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    list_c = my_list.copy()
    list_c.sort()
    return list_c[-1]
