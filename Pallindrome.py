# you are given a string you have to check whether the string is a pallindrome or not
# There are quiet a few ways to do it and the most efficient way is to use pointers
# because of the space complexity which is the least of O(1)

# CHECK pallindrome_4() function at the very last

# String Concatination
# Adding last element of the string to the new string and going on until we hit index 0.
# Space Complexity - O(n)
# Time Complexity - O(N**2)
# Time complexity is O(N**2) because the way string concatination works is O(N) which leads to nested for loop.
def pallindrome_1(s):
    new = ''
    for i in reversed(range(len(s))):
        new += s[i]
    return new == s

# This is the same method but instead of string we will use lists
# because appending into a list is a O(1) time
# Space Complexity - O(N)
# Time Complexity - O(N**2)
def pallindrome_2(s):
    new = []
    for i in reversed(range(len(s))):
        new.append(s[i])
    return "".join(new)==s

# Using recurssion to check this
# we will check first and the last element and then call the same function on the middle of the string
# Space Complexity - O(N)
# Time Complexity - O(N)
# Space Complexity is O(N) because most or maximum of the time when you use recurssion it works on the
# principle of call stack which does take a N space.
def pallindrome_3(s, i = 0):
    j = len(s)-1-i
    return True if i>=j else s[i]==s[j] and pallindrome_3(s, i+1)
"""
Tail recurssion may save you from taking O(N) spcae but that most of the time 
it depends on how strong your compiler is.
*(READ ABOUT IT)*
"""

# Using Pointers
# Checking wheather the first element is the same as the last element
# Incrementing the first index and decrementing the last index until both the pointer crosses eachother
# Spcae Complexity - O(!)
# Time Complexity - O(N)
def pallindrome_4(s):
    i = 0
    j = len(s) - 1
    while(i<j):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1 
    return True


s = input()
print(pallindrome_4(s))