#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if 0 <= x1 < x2 <= 10000 and 1 <= v1 <= 10000 and 1 <= v2 <= 10000:
            x = x2 - x1
            v = v1 - v2
            if v <= 0:
                return "NO"
            elif v > 0 and x % v == 0:
                return "YES"
            else:
                return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()