"""
https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1
"""
def duplicates(arr,n):
    # code here
    hash = {}
    lst = []
    for i in range(n):
        if arr[i] not in hash:
            hash[arr[i]] = 1
        else:
            if arr[i] not in lst:
                lst.append(arr[i])
    # lst = []
    # for item in hash:
    #     if hash[item]>1:
    #         lst.append(item)
    if lst==[]:
        return [-1]
    lst.sort()
    return lst

if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()
