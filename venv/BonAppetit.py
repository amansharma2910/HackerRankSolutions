#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    if 2 <= len(bill) <= 10**5 and 0 <= k <= len(bill):
        flag = 1
        sumOfItems = 0
        for i in bill:
            if 0 <= i <= 10**4:
                sumOfItems += i
            else:
                flag = 0
                break
        if flag == 1:
            bill = (sumOfItems - bill[k])/2
            if bill == b:
                print("Bon Appetit")
            else:
                print(int(b - bill))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
