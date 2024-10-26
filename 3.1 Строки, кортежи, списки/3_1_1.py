def main():
    ...


k = 0
for i in range(n := int(input())):
    a = input()
    if a[0] == 'а' or a[0] == 'б' or a[0] == 'в':
        k += 1
if k == n:
    print('YES')
else:
    print('NO')
if __name__ == "__main__":
    main()