#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    if 0 < n <= 100:
        for i in range(1,n+1):
            print(" "*(n-i) + "#"*(i))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
