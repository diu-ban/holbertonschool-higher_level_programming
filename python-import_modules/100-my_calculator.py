#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    l = len(argv)
    if (l != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    ops = {'+' : add, '-' : sub, '*' : mul, '/' : div}
    if op in ops:
        value = ops[op](a, b)
        print(f"{a} {op} {b} = {value}")
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    