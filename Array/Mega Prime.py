start = int(input())
end = int(input())
primes = [1]*(end+1)
primes[0] = primes[1] = 0
for i in range(4,end+1):
    if i%2==0:
        primes[i]=0
for i in range(3,end+1):
    if primes[i]==1:
        for i in range(i*i,end+1,i):
            primes[i]=0
total = 0
for i in range(start,end+1):
    if primes[i]==1:
        j = i
        flag = 0
        while j:
            if primes[j%10]==0:
                flag = 1
                break
            else:
                j = j//10
        if flag==0:
            total+=i
print(total)