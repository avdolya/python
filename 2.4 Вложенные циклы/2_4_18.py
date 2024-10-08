def main():
    ...


c = k = 1  
a = int(input())
st = ''
while k <= a:
    for i in range(c):
        if k > a:
            break
        st = st + str(k) + ' '
        k += 1  
    width = len(st[:-1])
    st = ''
    c += 1

k = 1
c = 1
while k <= a:
    for i in range(c):
        if k > a:
            break
        st = st + str(k) + ' '
        k += 1  
    print(f"{st[:-1]:^{width}}", end=' ')
    print()
    st = ''
    c += 1
if __name__ == "__main__":
    main()

 
