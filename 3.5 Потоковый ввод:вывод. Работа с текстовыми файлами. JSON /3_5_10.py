f = input()
n = int(input())
res = []
with open(f) as file_in:
    for line in file_in:
        res.append(line.rstrip('\n'))
for i in res[len(res) - n:len(res)]:
    print(i)

