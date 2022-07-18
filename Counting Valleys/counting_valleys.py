#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    num_valleys = 0
    for i in range(steps):
        if path[i] == 'U':
            altitude += 1
            
            
        if path[i] == 'D':
            altitude -= 1
        
        if path[i] == 'U' and altitude == 0:
            num_valleys += 1
    return num_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
