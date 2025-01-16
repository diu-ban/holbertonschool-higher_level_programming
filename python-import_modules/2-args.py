#!/usr/bin/python3
import sys

if __name__ == "__main__":
    l = len(sys.argv)
    print("{} arguments{}".format(l - 1, '.' if l < 2 else ':'))
    if (l >= 2):
        for i in range(l):
            print("{}:{}".format(i+1, sys.argv[i+1]))


