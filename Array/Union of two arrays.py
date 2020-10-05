"""
https://practice.geeksforgeeks.org/problems/union-of-two-arrays/0
"""
t = int(input())
while t:
    t-=1
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    lst = list(map(int,input().split()))
    val = set()
    val.update(arr)
    val.update(lst)
    print(len(val)