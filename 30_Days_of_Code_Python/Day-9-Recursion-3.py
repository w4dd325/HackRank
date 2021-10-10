#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # if input is 1 then we can do factorial
    if n <= 1:
        return 1
    else:
        # else n times by everything less than n
        # eg: n = 5     5 x 4 x 3 x 2 x 1
        result = n * factorial(n - 1)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
