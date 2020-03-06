#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    if 2 <= len(a) <= 100 and all(0 < i < 100 for i in a):
        b = list(set(a))
        c = [[i,j] for i in b for j in b if (i-j==1)]
        d = [a.count(i[0])+a.count(i[1]) for i in c] + [a.count(i) for i in b]
        if max(d) >= 2:
            return max(d)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
