# # Find the GCD of LCM of all unique pairs in an Array.
# """
# Given an integer array arr[] of size N,
# the task is to find the GCD of LCM of
# all unique pair (i, j) of the array,
# such that i < j.
# """
import math
import itertools
def LCM(x, y):
    return (x * y) // math.gcd(x, y)
def GCD(x,y):
    return math.gcd(x,y)
def pair(arr):
    return list(itertools.combinations(arr,2))

# Naive approach
# finding the unique pair
# finding the lcm of those pairs
# finding HCF
# def gcd_lcm(n,arr):
#     x = pair(arr)
#     lcm = []
#     for item in x:
#         lcm_val = LCM(item[0],item[1])
#         lcm.append(lcm_val)
#     gcd = 0
#     for i in range(len(lcm)):
#         gcd = GCD(gcd, lcm[i])
#     print(gcd)

#

# Python code to find the GCD of LCM
# of all unique pairs in an Array

from math import gcd
def gcd_lcm(n, arr):
    pre = [1]*n
    pre[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        pre[i] = gcd(arr[i],pre[i+1])
    lcm = []
    for i in range(n-1):
        y = LCM(arr[i], pre[i+1])
        lcm.append(y)
    ans = lcm[0]
    for i in range(1, n - 1):
        ans = gcd(ans, lcm[i])
    print(ans)

# main
n = int(input())
arr = list(map(int,input().split()))
gcd_lcm(n,arr)
