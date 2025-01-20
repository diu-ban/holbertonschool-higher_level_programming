#!/usr/bin/python3
def no_c(my_string):
    size = len(my_string)
    if (size == 0):
        return my_string
    return (my_string.translate({ord(i):None for i in 'Cc'}))
