"""
https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one/0
"""
#code
t = int(input())
while t:
    t-=1
    n = int(input())
    arr = list(map(int,input().split()))
    print(*([arr[-1]]+arr[:-1]))