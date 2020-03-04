#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    if 5 <= len(arr) <= 2*(10**5):
        birdData = {}
        for i in range(1,6):
            birdData[i] = arr.count(i)
        maxFreq = max(birdData.values())
        finalList = [k for k in birdData.keys() if birdData[k] == maxFreq]
        return finalList[0]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
