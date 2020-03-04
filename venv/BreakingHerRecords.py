#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    if 1 <= len(scores) <= 1000:
        flag = 1
        for i in scores:
            if 0 > i or i > 10**8:
                flag = 0
                break
        if flag == 1:
            maxScore = minScore = scores[0]
            highRec = lowRec = 0
            for i in scores:
                if i > maxScore:
                    highRec += 1
                    maxScore = i
                elif i < minScore:
                    lowRec += 1
                    minScore = i
            return [highRec, lowRec]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
