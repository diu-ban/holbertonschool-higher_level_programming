#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    if (size == 0 or size == 1):
        return
    my_list.reverse()
    for i in range(size):
        print("{}".format(my_list[i]))

