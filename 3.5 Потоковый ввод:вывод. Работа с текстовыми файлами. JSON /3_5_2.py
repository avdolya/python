from sys import stdin
lines = []
for line in stdin:
    lines.append(int(line.split()[2]) - int(line.split()[1]))
print(round(sum(lines) / len(lines)))
