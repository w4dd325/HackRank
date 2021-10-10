#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

        
    res = []

    # Use x and y ranges to move through the array
    # range(4) used as there is a maximum of 4 hour glasses available in grid
    # range() also has a default min value of 0
    #  1 2 3 4 5 6
    # |  1  |
    #   |  2  |
    #     |  3  |
    #       |  4  |
    for x in range(4):
        for y in range(4):
            # Calculate the sum of each hour glass
            # x = top line | x+1 = second line | x+2 = third line
            # y:y+3 takes value of y as starting point and y+3 for end point
            # x+1 & y+1 = the second row second column (center of hour glass)
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            # Use append to build list of all totals
            res.append(s)
    # Use max to get the highest value of res
    print(max(res))
