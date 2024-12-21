dict = {}
t = set()
res = []
for i in range(n := int(input())):
    a = input()
    a = a[a.find(':') + 2:].split(', ')
    for j in a:
        t.add(j)
    for toy in (t):
        dict[toy] = dict.get(toy, 0) + 1
    t = set()
for i in dict: 
    if dict.get(i, 0) == 1:
        res.append(i)
for i in sorted(res):
    print(i)
