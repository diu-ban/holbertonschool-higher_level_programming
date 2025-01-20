#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if (size == 0):
        return None
    if (idx < 0 or idx >= size):
        return None
    return my_list[idx]
