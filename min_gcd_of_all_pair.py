# Find minimum GCD of all pairs in an array
# Given an array arr of positive integers,
# the task is to find minimum GCD possible
# for any pair of the given array.

# this is simple the gcd of two number giving the min GCD
# in the list is the gcd of the whole list.

import math

def gcd_list(arr,n):
    g = 0
    for i in range(n):
        g = math.gcd(g,arr[i])
    print(g)

# main
n = int(input())
arr = list(map(int,input().split()))
gcd_list(arr,n)