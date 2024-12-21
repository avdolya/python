d = dict()
res = 0
n = int(input())
for i in range(n):
    a = input()
    d[a] = d.get(a, 0) + 1
for i in d:
    if d[i] > 1:
        res += d[i]
print(res)
