#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zeroNum = 0
    posNum = 0
    negNum = 0
    flag = 1
    for i in arr:
        if -100 <= i <= 100:
            if i > 0:
                posNum += 1
            elif i < 0:
                negNum += 1
            else:
                zeroNum += 1
        else:
            flag = 0
            break
    if flag == 1:
        print("{:06f}".format(posNum/len(arr)))
        print("{:06f}".format(negNum / len(arr)))
        print("{:06f}".format(zeroNum / len(arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
