set_1 = set()
arr = []
n = int(input()) 
m = int(input())    
for i in range(n + m):
    a = input()
    if a in set_1:
        set_1.remove(a)
    else:
        set_1.add(a)
for i in set_1:
    arr.append(i)
arr = sorted(arr)
if len(set_1) != 0:
    for i in arr:
        print(i)
else:
    print('Таких нет')
