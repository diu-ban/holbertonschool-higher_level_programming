#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = list(my_list)
    for i in range(len(new)):
        new[i] = replace if new[i] == search else new[i]
    return new
