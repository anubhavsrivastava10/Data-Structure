"""
Given A numbers of white and B numbers of black balls.
You need to have X number of white and Y number of black balls
(A <= X, B <= Y) to win the game by doing some(zero or more) operations.
"""
import math
def possibility(a,b,x,y):
    w = math.gcd(a,b)
    b = math.gcd(x,y)
    if w==b:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

# main
# given number of white(a) and black(b) balls
a,b = map(int,input().split())
# you have to have x white ball and y black ball
x,y = map(int,input().split())
possibility(a,b,x,y)