def main():
    ...


def prost(a):
    m = []
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            m.append(i)
            m.append(a // i)
    if len(m) == 2 and m[0] != m[1]:
        return 'yes'
    else:
        return 'no'
    

def delit(a):
    m = []
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            m.append(i)
            m.append(a // i) 
    m.sort()
    return m


c = int(input())
s = ''
res = ''
while c != 1:
    d = delit(c) 
    r = len(d) 
    if d == []:
        s += str(c) + " * "
        break
    else:
        for i in range(r):
            if prost(d[i]) == 'yes':
                k = i
                break
        c = c // d[k]
        s += str(d[k]) + " * "
print(s[:-3])
if __name__ == "__main__":
    main()