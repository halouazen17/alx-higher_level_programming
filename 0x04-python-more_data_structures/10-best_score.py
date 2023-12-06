#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_val = 0
    max_key = None
    for i, y in a_dictionary.items():
        if y > max_val:
            max_val = y
            max_key = i
    return max_key
