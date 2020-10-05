"""
https://practice.geeksforgeeks.org/problems/missing-number-in-array/0
"""
#code
t = int(input())
while t:
    t-=1
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    flag = 0
    for i in range(n-1):
        if arr[i]!=i+1:
            flag = 1
            print(i+1)
            break
    if flag==0:
        print(n)
        
    """
    Other Easy way could be
    """
    sum_of_n = n*(n+1)//2
    sum_of_arr = sum(arr)
    print(sum_of_n-sum_of_arr)