#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    if 1<= len(s) <= 100 and 1 <= d <= 31 and 1 <= m <= 12:
        flag = 1
        for i in s:
            if i < 1 or i > 5:
                flag = 0
                break
        if flag == 1:
            reqSet = 0
            for i in range((len(s)-m)+1):
                sumOfArr = 0
                for j in range(m):
                    sumOfArr += s[i+j]
                if sumOfArr == d:
                    reqSet += 1
            return reqSet

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
