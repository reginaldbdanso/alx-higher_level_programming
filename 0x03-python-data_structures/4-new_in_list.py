#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    if idx >= len(my_list):
        return my_list.copy()

    new_list = my_list.copy()
    new_list.pop(idx)
    new_list.insert(idx, element)
    return new_list