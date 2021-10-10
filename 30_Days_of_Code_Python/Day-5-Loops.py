#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    x = 1
    while x <= 10:
        print(str(n) + " x " + str(x) + " =", n * x)
        x += 1
