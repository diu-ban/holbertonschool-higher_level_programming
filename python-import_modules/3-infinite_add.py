#!/usr/bin/python3
import sys

if __name__ == "__main__":
    l = len(sys.argv)
    sum = 0
    if (l >= 2):
        for i in range(1,l):
            sum += int(sys.argv[i])
    print(sum)
