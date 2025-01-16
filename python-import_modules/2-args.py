#!/usr/bin/python3
import sys

if __name__ == "__main__":
    l = len(sys.argv)
    print("{} argument{}{}".format(l - 1, 's' if l != 1 else '', '.' if l < 2 else ':'))
    if (l >= 2):
        for i in range(l):
            print("{}:{}".format(i+1, sys.argv[i+1]))


