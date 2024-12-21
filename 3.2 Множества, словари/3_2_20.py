import math 


a = []
cnt = 0
k = set(input().split('; '))
for i in k:
    a.append(int(i))
a.sort()
for i in a:
    st = str(i) + (' - ')
    for j in a:
        if i != j:
            if math.gcd(int(i), int(j)) == 1:
                st += str(j) + ', '
                cnt += 1
    if cnt != 0:
        print(st[:-2])  
    cnt = 0            
