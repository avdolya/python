dict = {}
res = set()
while True:
    a = input().split()
    if a == []:
        break 
    else:
        if a[1] not in dict.get(a[0], []):
            dict[a[0]] = dict.get(a[0], []) + [a[1]]
        if a[0] not in dict.get(a[1], []):   
            dict[a[1]] = dict.get(a[1], []) + [a[0]]
for i in dict:
    dict[i].sort() 
for i in sorted(dict): 
    s = set()
    for j in dict[i]: 
        s = dict.get(j, []) 
        for x in s:
            res.add(x)
    res.remove(i)
    for j in dict[i]:
        if j in res:
            res.remove(j)
    print(f'{i}: {', '.join(sorted(res))}')
    s = set()
