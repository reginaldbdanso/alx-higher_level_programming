#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list != []:
        new_list = my_list.copy()
        for i in range(len(new_list)):
            if new_list[i] % 2:
                new_list[i] = False
            else:
                new_list[i] = True
    return new_list
