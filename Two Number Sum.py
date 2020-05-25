# You are given an array of Integers
# You are given a target sum
# You to find the pair of integers from the given array
# whose sum lines up to be the targetSum

# Naive Approach using two for loops

# time complex : O(N^2)
# Space complex : O(1)
def finding_pair(arr,targetSum):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==targetSum:
                print(arr[i],arr[j])
                # return arr[i],arr[j]
                # if you want the first pair whose sum is targetSum
                count+=1
    # return []
    return str(count)

# using hash table
# We are using the concept of x+y=targetSum
# where x is the value in the arr and y is the value in the hash table
# if y is present in the hash table we have found our pair

# time complexity : O(N)
# space complexity : O(N)
def finding_pair(arr,targetSum):
    hash=[]
    count=0
    for i in range(len(arr)):
        potential_sum = targetSum-arr[i]
        if (potential_sum) in hash:
            count+=1
            print(arr[i],potential_sum)
            hash.remove(potential_sum)
        else:
            hash.append(arr[i])
    return str(count)

# using the best approach
# sort the array and use two pointer from starting and from end.
# check the sum and move the pointer accordingly
# if the sum of array is greater than the targetSum move the right pointer
# or else move the left pointer
# if found the sum move both the pointer until left<right

# time complexity : O(N*log(N))   => N is the length of the array
# space complexity : O(N)
def finding_pair(arr,targetSum):
    arr.sort()
    count=0
    left=0
    right = len(arr)-1
    while(left<right):
        if arr[left]+arr[right]==targetSum:
            print(arr[left],arr[right])
            count+=1
            left+=1
            right-=1
        elif arr[left]+arr[right]>=targetSum:
            right-=1
        elif arr[left]+arr[right]<=targetSum:
            left+=1
    return str(count)


arr = [3,5,-4,8,5,-1,11,1,6]
# arr = list(map(int,input().split()))
targetSum = 10
# targetSum = int(input())
print("Pair found : " + finding_pair(arr,targetSum))