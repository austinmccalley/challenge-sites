#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # c is the array of clouds
    # n is the amount of clouds
    n = len(c)
    print(n)
    # if c[i] is 1 then it is bad
    # if c[i] is 0 then it is good

    # List of bad clouds
    bad_clouds = []
    for i in range(n):
        if int(c[i]) == 1:
            bad_clouds.append(i)

    print('Bad Clouds', bad_clouds)

    jumps = 0
    good_clouds = []


    for i in range(0, n):
        if i not in bad_clouds:
            good_clouds.append(i)

    print(good_clouds)

    curr_jumps = 0
    ctc = []

    for i in range(len(good_clouds)):
        curr_cloud = good_clouds[i]
        noc = good_clouds[i] + 1
        ntc = good_clouds[i] + 2

        print('Current cloud is ', curr_cloud)

        if (curr_cloud in ctc or curr_cloud == 0):
            if ntc in good_clouds:
                print('Jumping two clouds to ', ntc)
                curr_jumps += 1
                ctc.append(ntc)
            elif noc in good_clouds:
                print('Jumping one cloud to ', noc)
                curr_jumps += 1
                ctc.append(noc)
            else:
                print('END CASE')

    return curr_jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
