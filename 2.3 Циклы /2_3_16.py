def main():
    ...


k = 0
a = input()
for i in range(len(a) // 2):
    if a[i] == a[-i - 1]:
        k += 1
if k == len(a) // 2:
    print('YES')
else:
    print('NO')
if __name__ == "__main__":
    main()