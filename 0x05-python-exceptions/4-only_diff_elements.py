#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                val_1 = my_list_1[i]
                val_2 = my_list_2[i]
                if isinstance(val_1, (int, float)) and isinstance(val_2, (int, float)):
                    try:
                        division_result = val_1 / val_2
                        result_list.append(division_result)
                    except ZeroDivisionError:
                        print("division by 0")
                        result_list.append(0)
                else:
                    print("wrong type")
                    result_list.append(0)
            except IndexError:
                print("out of range")
                result_list.append(0)
    finally:
        return result_list
