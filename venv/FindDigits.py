#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    p = list(str(n))
    divisorCount = 0
    for i in p:
        try:
            if n % int(i) == 0:
                divisorCount += 1
        except ZeroDivisionError:
            continue
    return divisorCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
