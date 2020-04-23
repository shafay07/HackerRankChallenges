'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0
Output : 3
Sample Output 0
Output : Weird
'''

#!/bin/python3

import math
import os
import random
import re
import sys


# function to check weirdness of a number (n)
def weirdOrNot(input_n):
    if not n % 2 == 0:
        print('Weird')
    elif n % 2 == 0 and 2<n<=5:
        print('Not Weird')
    elif n % 2 == 0 and 6<n<=20:
        print('Weird')
    elif n % 2 == 0 and n>20:
        print('Not Weird')



if __name__ == '__main__':
    n = int(input().strip())
    if 1<=n<=100:
        weirdOrNot(n)
    else:
        print('try again')
