#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n % 2 == 0:
        n += 1
    pages = list(range(n+1))
    pagesCountFront = pages.index(p)
    turnFront = pagesCountFront//2
    pages.reverse()
    pagesCountBack = pages.index(p)
    turnBack = pagesCountBack//2
    return (turnFront if turnFront < turnBack else turnBack)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
