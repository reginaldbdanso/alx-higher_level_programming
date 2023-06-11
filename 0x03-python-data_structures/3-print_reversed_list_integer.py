#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for items in my_list:
        str = "{:d}"
        print(str.format(items))
