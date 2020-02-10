#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    meridian = s[len(s)-2:len(s)]
    time = s[:len(s) - 2]
    hr , mins , sec = map(int, time.split(":"))
    if 0 <= hr <= 12 and 0 <= mins <= 59 and 0 <= sec <= 59:
        if meridian == 'AM':
            if hr == 12:
                return "{:02d}:{:02d}:{:02d}".format(hr-12, mins, sec)
            else:
                return "{:02d}:{:02d}:{:02d}".format(hr, mins, sec)
        else:
            if hr == 12:
                return "{:02d}:{:02d}:{:02d}".format(12+(hr-12), mins, sec)
            else:
                return "{:02d}:{:02d}:{:02d}".format(12+hr, mins, sec)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()