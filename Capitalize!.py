# Link = https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    # for x in s[:].split():
    #     s = s.replace(x, x.capitalize())

    # return(s)
    
    s_cap = ""
    for i in range(len(s)):
        if(s[i-1]==" " and s[i].islower()) :
            s_cap = s_cap+s[i].upper()
        else :
            s_cap = s_cap + s[i]

    return (s_cap[0].upper()+s_cap[1:])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
