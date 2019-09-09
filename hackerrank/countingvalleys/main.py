#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # n is the number of steps       n = len(s)
    # s is the arr of the steps      DDUUDDUU
    n= int(n)
    elev = 0
    tsl = 0
    
    in_vall = False
    vals = 0


    for i in range(n):
        step = s[i]
        if step == 'D':
            elev -= 1
        elif step == 'U':
            elev += 1
        
        # In a valley
        if elev < 0:
            in_vall = True
        elif elev >= 0 and in_vall == True:
            in_vall = False
            vals +=1

    return vals

if __name__ == '__main__':
    

    f = open(r'C:\Users\mrmca\Documents\hackerrank\countingvalleys\input.txt', 'r')
    n, s = f.readlines()
    # print(n,s)

    # n = int(input())

    # s = input()

    result = countingValleys(n, s)
    print(result)



