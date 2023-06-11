#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # my_list.reverse()
    reversed_list = my_list[::-1]
    for items in reversed_list:
        print("{:d}".format(items))
