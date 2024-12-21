import json
a = input()
b = input()
res = dict()
with open(a, encoding="UTF-8") as file_in:
    users = json.load(file_in)
with open(b, encoding="UTF-8") as file_in:
    updates = json.load(file_in)
for i in users:
    name = i.pop('name')
    res[name] = i
for i in updates:
    name = i.pop('name')
    for j in i.keys():
        if res[name].get(j, '') < i[j]:
            res[name][j] = i[j]
with open(a, 'w') as file:
    json.dump(res, file, sort_keys=False, indent=4, ensure_ascii=False)
    