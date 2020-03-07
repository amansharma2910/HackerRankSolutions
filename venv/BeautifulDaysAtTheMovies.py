#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    noOfBeautifulDays = 0
    for m in range(i, j + 1):
        a = list(str(m))
        a.reverse()
        a = int(''.join(a))
        if (m - a) / k == (m - a) // k:
            noOfBeautifulDays += 1
    return noOfBeautifulDays

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
