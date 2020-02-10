#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    points = [0,0]
    flag = 1
    for i in range(3):
        if 1 <= a[i] <= 100 and 1 <= b[i] <= 100:
            if a[i] > b[i]:
                points[0] +=1
            elif a[i] < b[i]:
                points[1] +=1
        else:
            flag = 0
            break
    if flag == 1:
        return points

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
