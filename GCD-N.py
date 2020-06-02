"""
Find the sum of GCD of all numbers upto N with N itself.
N = 12
Output = 40
(1,12) = 1,(2,12) = 2,(3,12) = 3, so on and so forth until (12,12) = 12
add them up  (1 + 2 + 3 + 4 + 1 + 6 + 1 + 4 + 3 + 2 + 1 + 12) = 40.
"""

# naive approach is iterating through a loop and adding them each
# time complexity : N*log(N)

import math
def sumofgcd(n):
    gcd_sum = 0
    for i in range(1,n+1):
        gcd_sum += math.gcd(i,n)
    print(gcd_sum)

# optimising the above approach
# finding the divisor of the number and the number of count for each divisor
# time complexity : O(N)
def get_count(d,n):
    no = n//d
    result = no
    p = 2
    while(p*p<=no):
        if no%p==0:
            while(no%p==0):
                no //= p
            result -= result//p
    if no>1:
        result -= result//no
    return result

def sumofgcd(n):
    res = 0
    i = 1
    while(i*i<=n):
        d1 = i
        d2 = n//i
        res += d1 * get_count(d1,n)
        if d1!=d2:
            res += d2 * get_count(d2,n)
        i+=1
    print(res)

n = int(input())
sumofgcd(n)