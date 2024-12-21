from sys import stdin
lines = []
res = []
for line in stdin:
    lines += line.split()
for i in lines:
    if i.lower() == i.lower()[::-1]:
        res.append(i)
for i in sorted(set(res)):
    print(i)