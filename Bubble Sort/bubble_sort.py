#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#
from itertools import product
def countSwaps(a):
    # Write your code here
    no_of_swaps = 0
    for i, j in product(range(len(a)), range(len(a) - 1)):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                no_of_swaps += 1
    print("Array is sorted in {0} swaps.".format(no_of_swaps))
    print("First Element: {0}".format(a[0]))
    print("Last Element: {0}".format(a[-1]))
if __name__ == '__main__':
    n = int(raw_input().strip())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a)
