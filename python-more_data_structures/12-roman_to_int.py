#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 
    roman = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    sum = 0
    size = len(roman_string)
    for i in range(size):
        if i < size - 1 and roman[roman_string[i]] < roman[roman_string[i+1]] :
            sum -= roman[roman_string[i]]
        else:
            sum += roman[roman_string[i]]
    return sum
