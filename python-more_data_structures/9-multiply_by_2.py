#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return
    new = dict(a_dictionary)
    for key in new:
        new[key] *= 2
    return new