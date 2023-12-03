#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    val = len(my_list)
    copy = my_list.copy()
    if idx < 0 or idx >= val:
        return (my_list)
    copy[idx] = element
    return copy
