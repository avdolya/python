d = dict()
sm = 0
while True:
    a = input()
    if a == "":
        break 
    else:
        a = a.split()
        for i in a:
            d[i] = d.get(i, 0) + 1
for i in d:
    print(f"{i} {d[i]}")
