#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    #Create empty list
    validNamesList = []
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        
        #emailID is the second input, search it for the string "@gmail.com"
        if emailID.find("@gmail.com") != -1: #!= -1 means string was found
            #add first name to list
            validNamesList.append(firstName)
            
    for i in sorted(validNamesList):
        print(i)
