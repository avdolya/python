def main():
    ...


def prost(a):
    m = []
    for i in range (1, int(a ** 0.5) + 1):
        if a % i == 0:
            m.append(i)
            m.append(a // i)
    if len(m) == 2 and m[0] != m[1]:
        return ('yes')
    else:
        return('no')
    

def delit(a):
    m = []
    for i in range (2, int(a ** 0.5) + 1):
        if a % i == 0:
            m.append(i)
            m.append(a // i) 
    m.sort()
    return m

s = ''
c = int(input())
#print(delit(c), prost(c))
while c != 1:
    for i in range(len(delit(c))):
        if prost(delit(c)[i]) == 'yes':
            s = s + str(delit(c)[0]) + ' * '
            c = c // delit(c)[0]
            break
print(s)       
if __name__ == "__main__":
    main()