# Check if the square of a number(x) is divisible by K or not.
# you have to check if (x^2) % k == 0.
# where x lies in between [1, 10^18].

def check_xk(x,k):
    x = x**2
    # but for x in range 10^18 it will take a long time.
    if x%k==0:
        print('YES')
    else:
        print('NO')

# another effective approach
# instead of finding x**2 which will give you memory overflow
# find the gcd of x and k and reduce the value of k.
# then check that x%k==0 or not.
import math
def check_xk(x,k):
    # finding gcd of x,k
    g = math.gcd(x, k)
    # updating k
    k = k//g
    # check if x is divisible by reduced k
    if x%k==0:
        print('YES')
    else:
        print('NO')

# main
x = int(input())
k = int(input())
check_xk(x,k)