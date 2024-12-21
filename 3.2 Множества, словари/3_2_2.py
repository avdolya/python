st = ''
a = set(input())
b = set(input())
res = a & b
for i in res:
    st += i
print(st)
