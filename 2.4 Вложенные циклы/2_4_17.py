def main():
    ...


def pal(a):
    if a[::-1] == a:
        return 'yes'
    else:
        return 'no'


k = 0
n = int(input())
for i in range(n):
    a = input()
    if pal(a) == 'yes':
        k += 1
print(k)
if __name__ == "__main__":
    main()