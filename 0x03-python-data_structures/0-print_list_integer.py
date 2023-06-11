#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for items in my_list:
        str = "{:d}"
        print(str.format(items))
