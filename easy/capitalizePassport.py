'''
Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import string 
# Complete the solve function below.
def solve(s):
    if len(s) > 0 and len(s) < 1000:
        answer = string.capwords(s, ' ')
        return answer 
        ##if not return statement, it will not work
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

'''
Unsupported operand type(s) for +: 'NoneType' and 'str' #

Cause: 
The most common sources of None values are:

Having a function that doesn't return anything (returns None implicitly).
Explicitly setting a variable to None.
Assigning a variable to the result of calling a built-in function that doesn't return anything.
Having a function that only returns a value if a certain condition is met.
Make sure you aren't calling a function that doesn't return anything and expecting the return value to be a string.
'''