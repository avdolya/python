from sys import stdin
lines = []
for line in stdin:
    lines += [int(i) for i in line.split()]

print(sum(lines))