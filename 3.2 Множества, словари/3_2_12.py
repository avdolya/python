d = dict()
k = 0
arr = []
n = int(input())
for i in range(n):
    a = input()
    d[a] = d.get(a, 0) + 1
for i in d:
    if d[i] > 1:
        arr.append(f'{i} - {d[i]}')
    else:
        k += 1
arr = sorted(arr)
if k == len(d):
    print('Однофамильцев нет')
else:
    for i in arr:
        print(i)



