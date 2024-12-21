s = set()
for i in range(n := int(input())):
    a = input().split(' ')
    for i in a:
        s.add(i)
for i in s:
    print(i)      
