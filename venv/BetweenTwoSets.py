#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    a.sort()
    b.sort()
    if 1 <= len(a) <= 1000 and 1 <= len(b) <= 1000:
        flag = 1
        for i in a:
            if i > 100 or i < 1:
                flag = 0
                break
        for j in b:
            if j > 100 or j < 1:
                flag = 0
                break
        if flag == 1:
            iniList = []
            for k in range(max(a), min(b) + 1):
                flag = "T"
                for i in a:
                    if k % i != 0:
                        flag = "F"
                        break
                if flag == "T":
                    iniList.append(k)
            finalList = []
            for k in iniList:
                flag = "T"
                for m in b:
                    if m % k != 0:
                        flag = "F"
                        break
                if flag == "T":
                    finalList.append(k)
            return len(finalList)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
