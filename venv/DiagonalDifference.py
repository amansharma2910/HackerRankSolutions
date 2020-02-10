#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# for i in arr:
#         for j in i:
#             if -100 <= j <= 100:
#                 pass
#             else:
#                 flag = 0
#                 break
#     if flag == 1:
def diagonalDifference(arr):
    flag = 1
    leftDiagonal = 0
    rightDiagonal = 0
    for i in range(len(arr)):
        leftDiagonal += arr[i][i]
        rightDiagonal += arr[i][len(arr)-1-i]
    return abs(rightDiagonal-leftDiagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()