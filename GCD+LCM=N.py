# Print any pair of integers with sum of GCD and LCM equals to N

# you are given a number N
# find the pair of number whose LCM + GCD = N
# eg N=14  (1,13) LCM = 13 GCD = 1 (13+1 = 14)

# Approach
# GCD of any  number with 1 is always 1
# GCD(1, N) = 1
# LCM of any number with 1 is that number itself
# LCM(1, N) = N

def sum_gcd_lcm(N)
    num1 = 1
    num2 = N-1
    print(num1, num2)

n = int(input())
sum_gcd_lcm(n)