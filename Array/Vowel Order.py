vowels = ['a','e','i','o','u']
lst = list(map(str,input().split()))
dic = {}
for item in lst:
    if item in dic:
        dic[item]+=1
    else:
        dic[item] = 1
val = []
for item in dic:
    if dic[item]>1 and item!='.':
        pp = len(item)
        c = chr(94)
        flag = 0
        for i in range(pp):
            if ord(item[i]) < 95:
                if item[i] in vowels:
                    if chr(ord(item[i])+32)<c:
                        flag = 1
                        break
                    else:
                        c = item[i]
            else:
                if item[i] in vowels:
                    if chr(ord(item[i]))<c:
                        flag = 1
                        break
                    else:
                        c = item[i]
        if flag==0:
            val.append(item)
            val.append(dic[item])
print(*val)
