def main():
    pass
a = str(int(input()))
b = str(int(input()))
n1 = []
n2 = []
res = []
res1 = ''
while len(a) != len(b):
    if len(a) > len(b):
        b = '0' + b
    else:
        a = '0' + a
for i in range(len(a)):
    n1.append(a[i])
    n2.append(b[i])
for i in range(len(a)):
    res.append(str((int(n1[i]) + int(n2[i])) % 10))
for i in range(len(res)):
    res1 += res[i]
print(res1)
if __name__ == '__main__':
    main()
