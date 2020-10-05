"""
https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1
"""
#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        hash = {}
        for i in range(n):
            if arr[i] not in hash:
                hash[arr[i]] = 1
            else:
                hash[arr[i]] += 1
        count = 0
        for i in range(n):
            need = k-arr[i]
            if need in hash:
                count+=hash[need]
            if need == arr[i]:
                count-=1
        return count//2

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1