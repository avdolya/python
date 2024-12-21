dict = {}
arr = []
n = int(input())
for i in range(n):
    m = input().split()
    dict[m[0]] = ''.join(m[1:])
kasha = input()
for i in dict:
    if kasha in dict[i]:
        arr.append(i)
if len(arr) != 0:
    for i in sorted(arr):
        print(i)
else:
    print('Таких нет')
