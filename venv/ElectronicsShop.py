#!/bin/python3

import os
import sys


#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    if 1 <= len(keyboards) <= 1000 and 1 <= len(drives) <= 1000 and 1 <= b <= 10 ** 6 and min(keyboards) >= 1 and max(
            keyboards) <= 10 ** 6 and min(drives) >= 1 and max(drives) <= 10 ** 6:
        totPrice = [i + j for i in keyboards for j in drives if (i + j <= b)]
        try:
            return max(totPrice)
        except:
            return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
