from sys import stdin
lines = []
for line in stdin:
    lines.append(line)

for i in lines[:-1]:
    if lines[-1].lower().strip('\n') in i.lower().strip('\n'):
        print(i.strip('\n'))