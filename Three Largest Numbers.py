"""
Consider an array of numbers which may or maynot be sorted
You have to find out the three largest number from the array
"""

"""
This is just sortung the array and picking up the last three elements.
"""
# def threeNumSum(arr, n):
#     # the dumb way would be
#     arr.sort()
#     return arr[-1]+arr[-2]+arr[-3]

"""
# Time Complexity - O(n)
# Space Complexity - O(1)
In this approach we are intalizing the array of size three with a None value in it
Then we iterating through each number and checking
If the number is greater than the any element in the array of size three then we place the 
number accordingly and shift the array towards the left while discarding the 
very left element of the array.
"""
def threeNumLargest(arr, n):
    largest = [None, None, None]
    for num in arr:
        update(largest, num)
    return largest

def update(largest, num):
    if largest[2] is None or largest[2]<num:
        shiftarray(largest, num, 2)
    elif largest[1] is None or largest[1]<num:
        shiftarray(largest, num, 1)
    elif largest[0] is None or largest[0]<num:
        shiftarray(largest, num, 0)

def shiftarray(largest, num, idx):
    for i in range(idx+1):
        if i == idx:
            largest[i]=num
        else:
            largest[i] = largest[i+1]


# Size of the array
n = int(input())
# Actual Array
arr = map(int,input().split())
print(threeNumLargest(arr, n))