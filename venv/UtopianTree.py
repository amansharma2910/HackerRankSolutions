#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    counter = 0
    treeHeight = 0
    while counter<=n:
        if counter%2 == 0:
            treeHeight += 1
        else:
            treeHeight *= 2
        counter += 1
    return treeHeight

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
