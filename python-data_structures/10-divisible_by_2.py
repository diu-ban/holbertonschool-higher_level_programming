#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    result = []
    for ele in my_list:
        result.append(True if ele % 2 == 0 else False)
    return result
