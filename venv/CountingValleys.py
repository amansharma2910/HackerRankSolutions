#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    if 2 <= n <= 10**6:
        noOfValleys = 0
        levelIndicator = {"U":1, "D":-1}
        seaLevel = 0
        for i in s:
            seaLevelIni = seaLevel
            seaLevel += levelIndicator[i]
            if seaLevelIni >= 0 and seaLevel < 0:
                noOfValleys += 1
        return noOfValleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
