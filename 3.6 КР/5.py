import json
from sys import stdin
import json
d = dict()
pr = set()
def prost(x):
    st = ''
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            st = st + str(i) + str(x//i)
    if st == '1' + str(x):
        return 1
    else:
        return 0
lines = []
for line in stdin:
    lines.append(line.rstrip('\n'))
for line in lines:
    for i in range(1, int(int(line) ** 0.5) + 1):
        if prost(i) and int(line) % i == 0 and i != 1:
            pr.add(i)
            d[i] = []
        elif int(line) % i == 0 and prost(int(line) // i):
            pr.add(i)
            d[i] = []
for line in lines:
    for j in d:
        if int(line) % int(j) == 0 and line not in d.get(j, []):
            d[j] = d.get(j, []) + [line]
for j in d:
    d[j].sort()
with open('result.json') as file_out:
    json.dump(d, file_out, ensure_ascii=False, indent=2)
