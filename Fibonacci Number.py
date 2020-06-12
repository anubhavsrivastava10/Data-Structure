# Your goal is to find the nth fibbo number

# Naive Approach
def fibbo(n):
    if n<=1:
        return n
    else:
        return fibbo(n-1)+fibbo(n-2)

# Better Approach
# Iterative Solution by far the best approach
# Time Complexity - O(n)
# Space Complexity - O(1)
def fibbo(n):
    a = 0
    b = 1
    if n <= 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b

# Using Memoization
# time Complexity - O(n)
# space Complexity - O(n)
def fibbo(n, memoize = {1: 0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fibbo(n-1, memoize)+fibbo(n-2, memoize)
        return memoize[n]
# Using formula to find the Nth fibbo number
import math
def fibbo(n):
    fib = ((pow((1 + math.sqrt(5)), n-1) -
            pow((1 - math.sqrt(5)), n-1)) /
           (pow(2, n-1) * math.sqrt(5)))

    return int(fib)

# You can also print the sequence using the same way
def fibo_sequence(n):
    fib = 0
    for i in range(n):
        fib = ((pow((1 + math.sqrt(5)), i) -
                pow((1 - math.sqrt(5)), i)) /
               (pow(2, i) * math.sqrt(5)))
        print(int(fib), end=' ')

print(fibbo(100))
fibo_sequence(100)