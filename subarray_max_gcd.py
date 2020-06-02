# Length of longest subarray of length at least 2 with maximum GCD
# you are given N the size of array and arr the array itslef.
# find the longest subsequence(consecutive) having the greatest GCD.

# naive approach is to find all possible subsequence of atleast size to
# using two for loops
# time complexity : O(N^2)

# Effective Approach
from math import gcd
def longsub_gcd(n,arr):
    if n==1:
        return 0
    k = 1
    # finding the GCD of the two consecutive element.
    for i in range(1,n):
        k = max(k, gcd(arr[i],arr[i-1]))
    # you have found the max of the pair for the given array.
    count = 0
    maxlen = 0
    # checking if there is more than 2 numbers for a pair.
    for i in range(n):
        if arr[i]%k==0:
            count+=1
        else:
            maxlen = max(maxlen,count)
            count = 0
    # finding the longest sequence.
    maxlen = max(maxlen, count)
    return maxlen

# main
N = int(input())
arr = list(map(int,input().split()))
print(longsub_gcd(N,arr))