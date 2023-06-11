#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) is not list:
        pass
    else:
        my_list.reverse()
        for items in my_list:
            print("{:d}".format(items))
