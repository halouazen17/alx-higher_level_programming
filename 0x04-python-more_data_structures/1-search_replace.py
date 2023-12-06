#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda y: replace if y == search else y, my_list))
