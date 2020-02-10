#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sum = 0
    flag = 1
    for i in arr:
        if 1 <= i <= 10**9 :
            sum += i
        else:
            flag = 0
            break
    if flag == 1:
        print((sum - arr[-1]), (sum - arr[0]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)