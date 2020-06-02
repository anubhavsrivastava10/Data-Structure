# Split N natural numbers into two sets having GCD of their sums greater than 1
# You are given the number N you have to split it into two groups.
# where you have numbers [1,2,3,.....N] until N.
# GCD(sum(set1),sum(set2)) = answer where answer > 1.
# GCD(sum(2,4),sum(1,3,5)) = 3 for N = 5.
# if not possible output is -1.

import math
# creating a pair of even and odd.
# time complexity = O(N)
def set_of_pair1(n):
    if n<=2:
        print(-1)
    else:
        set1=[]
        set2=[]
        for i in range(1, n+1):
            if i%2==0:
                set1.append(i)
            else:
                set2.append(i)
        # you dont need to do this just confirming the answer.
        x = sum(set1)
        y = sum(set2)
        check = math.gcd(x, y)
        # validating the answer
        print("max gcd : " + str(check))
        # printing set
        print(*set1)
        print(*set2)

# another approach
"""
If N is odd:
    The sum of N natural numbers is divisible by (N+1)/2 in this case.
    Therefore we only need to put (N+1)/2 into first set and the remaining numbers into second set.
    This will automatically make the GCD of their sums greater than 1.
If N is even:
    The sum of N natural numbers is divisible by N/2 in this case.
    Therefore we only need to put N/2 into first set and the remaining numbers into second set.
    This will automatically make the GCD of their sums greater than 1.
"""

def set_of_pair(n):
    if n<=2:
        print(-1)
    else:
        if n%2==0:
            set1 = n//2
        else:
            set1 = (n+1)//2
        set2 = []
        for i in range(1,n+1):
            if i!=set1:
                set2.append(i)
        # validating check(not necessary)
        y = sum(set2)
        gcd = math.gcd(set1,y)
        print(gcd)
        # printing sets
        print(set1)
        print(*set2)
# main
N = int(input())
set_of_pair(N)