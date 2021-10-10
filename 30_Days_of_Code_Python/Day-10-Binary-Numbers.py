#!/bin/python3

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    n = int(input().strip())
    
    # convert decimal to binary using bin()
    # use [2:] to remove the ob from start of output
    bin_output = bin(n)[2:]
    #print(bin_output)
    
    count = 0
    total_count = 0
    for i in bin_output:
        # convert to int as count wasn't recognising it.
        z = int(i)
        #print("i ----", z)
        if z is 1:
            count += 1
            #print("1 count = ", count)
            
            # if current count is higher than previous counts then update total_count
            if count > total_count:
                total_count = count
        else:
            count = 0
            #print("0 count = ", count)
    print(total_count)
