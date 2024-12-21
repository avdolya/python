s = []
k = 0
a = input()
with open(a) as file_in:
    for line in file_in:
        s += list(map(int, line.split()))
print(len(s))
for i in s:
    if i > 0:
        k += 1
print(k)
print(min(s))
print(max(s))
print(sum(s))
print(round(sum(s) / len(s), 2))
