# GCD

# Naive Approach
def gcd(a,b):
    max_val = 1
    for i in range(2,a+b):
        if a%i == 0 and b%i==0:
            max_val = i
    print(max_val)

# Each steps reduces the numbers by about the factor of 2
# Time Complexity - O(log(ab))
# So for appx 100 digit numebr it will take around 600 steps.
def gcd(a,b):
    flag = 0
    while(flag == 0):
        if a<=b:
            b = b%a
        else:
            a = a%b
        if a==0 or b==0:
            flag = 1
    print(b)

# main
a,b = map(int,input().split())
gcd(a,b)