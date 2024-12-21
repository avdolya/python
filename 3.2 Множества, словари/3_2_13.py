dict = {}
arr = []
n = int(input())
for i in range(n):
    dict[input()] = 0
m = int(input())
for i in range(m):
    a = int(input())
    for j in range(a):
        x = input()
        dict[x] = dict.get(x, 0) + 1
for i in dict:
    if dict[i] == 0:
        arr.append(i)
if len(arr) != 0:
    for i in sorted(arr):
        print(i)
else:
    print('Готовить нечего')
