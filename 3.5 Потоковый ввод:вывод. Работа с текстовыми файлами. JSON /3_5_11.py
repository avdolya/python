import json
file1 = input()
file2 = input()
s = []
k = 0
d = dict()
with open(file1) as file_in:
    for line in file_in:
        s += list(map(int, line.split()))
for i in s:
    if i > 0:
        k += 1
d['count'] = len(s)
d['positive_count'] = k
d['min'] = min(s)
d['max'] = max(s)
d['sum'] = sum(s)
d['average'] = round(sum(s) / len(s), 2)
with open(file2, "w", encoding="UTF-8") as file_out:
    json.dump(d, file_out, ensure_ascii=False, indent=2)