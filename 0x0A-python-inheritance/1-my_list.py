#!/usr/bin/python3
"""
my_list module inherits from list and
prints out in sorted order
"""


class MyList(list):
    """MyList class inherits from list"""
    def print_sorted(self):
        """prints list in sorted order"""
        print(sorted(self))
