set_1 = set()
n = int(input()) 
m = int(input())    
for i in range(n + m):
    a = input()
    if a in set_1:
        set_1.remove(a)
    else:
        set_1.add(a)
if len(set_1) != 0:
    print(len(set_1))
else:
    print('Таких нет')
