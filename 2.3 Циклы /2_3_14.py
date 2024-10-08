def main():
    ...


a = int(input())
m = []
for i in range(1, int(a ** 0.5) + 1):
    if a % i == 0:
        m.append(i)
        m.append(a // i)
if len(m) == 2 and m[0] != m[1]:
    print('YES')
else:
    print('NO')
if __name__ == "__main__":
    main()