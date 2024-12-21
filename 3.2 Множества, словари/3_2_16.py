a = []
res = set()
while True:
    a = input().split()
    if a == []:
        break 
    else:
        for i in range(len(a)):
            if a[i] == 'зайка':
                if i != 0:
                    res.add(a[i - 1])
                if i + 1 != len(a):
                    res.add(a[i + 1])
for i in res:
    print(i)
