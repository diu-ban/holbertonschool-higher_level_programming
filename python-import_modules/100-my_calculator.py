#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    l = len(sys.argv)
    if (l != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    ops = {'+' : add, '-' : sub, '*' : mul, '/' : div}
    if op in ops:
        value = ops[op](sys.argv[1], sys.argv[3])
        print(f"{sys.argv[1]} {op} {sys.argv[3]} = {value}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")

    