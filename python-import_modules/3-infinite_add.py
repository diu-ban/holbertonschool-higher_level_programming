#!/usr/bin/python3
import sys

if __name__ == "__main__":
    l = len(sys.argv)
    sum = 0
    if (len >= 2):
        for i in range(l):
            sum += int(sys.argv[l+1])
    print(sum)
    