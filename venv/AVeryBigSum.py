#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    flag = 1
    for i in ar:
        if 0 <= i <= 10**10:
            sum += i
        else:
            flag = 0
            break
    if flag == 1:
        return sum


if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print(result)
