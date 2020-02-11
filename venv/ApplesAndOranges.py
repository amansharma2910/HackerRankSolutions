#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    flag = 1
    if 1 <= (s and t and a and b) <= 10**5 and a<s<t<b:
        for i in apples:
            if -10**5 > i or i > 10**5:
                flag = 0
                break
        for j in oranges:
            if -10**5 > j or j > 10**5:
                flag = 0
                break
    else:
        flag = 0

    if flag == 1:
        apple_in_house = 0
        orange_in_house = 0
        for i in range(len(apples)):
            apples[i] += a
            if s <= apples[i] <= t:
                apple_in_house += 1
        print(apple_in_house)
        for j in range(len(oranges)):
            oranges[j] += b
            if s <= oranges[j] <= t:
                orange_in_house += 1
        print(orange_in_house)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)