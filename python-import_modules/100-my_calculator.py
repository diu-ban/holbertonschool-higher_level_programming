#!/usr/bin/python3
import sys
import calculator_1

if __name__ == "__main__":
    l = len(sys.argv)
    if (l != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    ops = {'+' : calculator_1.add, '-' : calculator_1.sub, '*' : calculator_1.mul, '/' : calculator_1.div}
    if op in ops:
        value = ops[op](sys.argv[1], sys.argv[3])
        print(f"{sys.argv[1]} {op} {sys.argv[3]} = {value}")
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    