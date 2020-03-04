#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    if 2 <= n <= 100 and 1 <= k <= 100:
        flag = 1
        for i in ar:
            if i < 1 or i > 100:
                flag = 0
                break
        if flag == 1:
            pairCounter = 0
            for j in range(n-1):
                for i in range(j+1, n):
                    if (ar[j] + ar[i]) % k == 0:
                        pairCounter += 1
            return pairCounter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
