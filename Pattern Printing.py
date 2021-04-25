# Rectangle Pattern

#Full rectangle
def full_rect(n,m):
    for i in range(n):
        for j in range(m):
            print("*",end=" ")
        print()
# full_rect(5,5)

# Hollow rectangle
def hollow_rect(n,m):
    for i in range(n):
        if i==0 or i==n-1:
            for j in range(m):
                print('*', end = " ")
        else:
            for j in range(m):
                if j==0 or j==m-1:
                    print("*", end = " ")
                else:
                    print(" ",end=" ")
        print()
# hollow_rect(5,10)

# Half Pyramid
def half_pyramid(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*',end= ' ')
        print()
# half_pyramid(5)

#inverted half pyramid
def inv_half_pyd(n):
    for i in range(n,0,-1):
        for j in range(i):
            print('*', end = ' ')
        print()
# inv_half_pyd(5)

#hollow inverted half pyramid
def hollow_inv_half_pyd(n):
    for i in range(n,0,-1):
        if i==n:
            for j in range(i):
                print('*', end = " ")
        else:
            for j in range(i):
                if j==0 or j==i-1:
                    print('*',end= " ")
                else:
                    print(' ',end= " ")
        print()
# hollow_inv_half_pyd(10)

#full pyramid
def full_pyd(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end=' ')
        for j in range(i):
            print('*',end='   ')
        print()
# full_pyd(6)

#inverted full pyramid
def inv_full_pyd(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ',end = ' ')
        for j in range(i):
            print('*', end = "   ")
        print()
# inv_full_pyd(5)

#hollow full pyramid
def hol_full_pyd(n):
    for i in range(1,n+1):
        if i!=n:
            for j in range(n-i):
                print(' ', end = ' ')
            for j in range(i):
                if j==0 or j==i-1:
                    print('*', end = '   ')
                else:
                    print(" ", end = '   ')
        else:
            for j in range(i):
                print('*',end = '   ')
        print()
# hol_full_pyd(10)

#number pyramid
def num_pyd(n):
    for j in range(1,n+1):
        for i in range(1,j+1):
            print(i,end= ' ')
        print()
# num_pyd(5)

#number pyramid in reverse
def num_pyd_rev(n):
    for j in range(n,0,-1):
        for i in range(1,j+1):
            print(i,end= ' ')
        print()
# num_pyd_rev(5)

#hollow number pyramid
def hollow_num_pyd(n):
    for j in range(1,n+1):
        for i in range(1,j+1):
            if (i==1 or i==j):
                print(i,end=' ')
            elif j==n:
                print(i,end=' ')
            else:
                print(' ',end = ' ')
        print()
# hollow_num_pyd(5)

#full number pyramid
def full_num_pyd(n):
    k = 0
    for i in range(1,n+1):
        k+=1
        p = k
        for j in range(n-i):
            print(' ',end = ' ')
        for j in range(1,i+1):
            print(p,end = ' ')
            p+=1
        for j in range(i,1,-1):
            print(p-2,end=' ')
            p-=1

        print()
# full_num_pyd(5)

#hollow full number pyramid
def hol_full_num_pyd(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ', end = ' ')
        for j in range(1,i+1):
            if j==1 or j==i or i==n:
                print(j,end= '   ')
            else:
                print(' ',end = '   ')
        print()
# hol_full_num_pyd(5) 

#hollow inverted number half pyramid
def hol_inv_half_pyd(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            if i==n or j==1 or j==i:
                print(j,end= ' ')
            else:
                print(' ',end= ' ')
        print()
# hol_inv_half_pyd(5)

# pallindromic half pyramid
def pallindromic_half_pyd(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print(j,end= ' ')
        for j in range(i,0,-1):
            print(j,end = ' ')
        print()
# pallindromic_half_pyd(5)

# pallindromic half pyramid with alphabets
def pallindromic_half_pyd_alpha(n):
    for i in range(1,n+1):
        p = 65
        for j in range(1,i):
            print(chr(p),end = ' ')
            p+=1
        for j in range(i,0,-1):
            print(chr(p),end = ' ')
            p-=1
        print()
# pallindromic_half_pyd_alpha(5)

# pallindromic full pyramid
def pallindromic_full_pyd(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end= ' ')
        for j in range(1,i):
            print(j,end=' ')
        for j in range(i,0,-1):
            print(j,end=' ')
        print()
# pallindromic_full_pyd(5)

# pallindromic * pyramid
def pallindromic_pyd_design(n):
    t = 1
    for i in range(1,n+1):
        for j in range(n-i+1):
            print('*',end='')
        for j in range(i):
            print(t,end='*')
        for j in range(n-i):
            print('*',end='')
        t+=1
        print()
# pallindromic_pyd_design(8)

# Diamond pattern
def diamond(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end='')
        for j in range(2*i-i):
            print('*',end=' ')
        print()
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(' ',end='')
        for j in range(i):
            print('*',end = ' ')
        print()
# diamond(10)

# hollow diamond pattern
def hollow_diamond(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end='')
        for j in range(2*i-i):
            if j==0 or j==2*i-i-1:
                print('*',end = ' ')
            else:
                print(' ',end=' ')
        print()
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(' ',end='')
        for j in range(2*i-i):
            if j==0 or j==2*i-i-1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
# hollow_diamond(5)

# solid half traingle
def semi_diamond(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*',end='')
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print('*',end='')
        print()
# semi_diamond(5)

# Floyd's Traingle Pattern
def floyd(n):
    k = 1
    for i in range(1,n+1):
        for j in range(i):
            print(k,end = ' ')
            k+=1
        print()
# floyd(5)

# pascals triangle
def pascals(n):
    for i in range(1,n+1):
        c = 1
        for j in range(1,i+1):
            print(c,end=' ')
            c = int(c*(i-j)/j)
        print()
# pascals(6)
