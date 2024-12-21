from sys import stdin
import json
lines = []
d = dict()
name = input()
with open(name, encoding="UTF-8") as file_in:
    records = json.load(file_in)
for line in stdin:
    lines.append(line.rstrip("\n"))
for line in lines:
    d[line.split(' == ')[0]] = line.split(' == ')[1]
for i in d:
    records[i] = d[i]
with open(name, "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)

