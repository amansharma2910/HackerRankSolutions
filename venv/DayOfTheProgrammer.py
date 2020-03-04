#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    progDay = lambda year: ("12.09.{}".format(year) if (
                year % 4 == 0 and ((year % 100 != 0) or ((year % 100 == 0) and (year % 400 == 0)))) else (
        "26.09.1918" if year == 1918 else "13.09.{}".format(year))) if 1918 <= year <= 2700 else (
        "12.09.{}".format(year) if year % 4 == 0 else "13.09.{}".format(year))
    return progDay(year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
