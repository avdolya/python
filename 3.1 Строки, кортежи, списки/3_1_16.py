def main():
    ...


arr = []
lnn = int(input())
all_l = ln = 0
n = int(input())
for i in range(n):
    a = input()
    all_l += len(a)
    arr.append(a)
for m in arr:
    ln += len(m) 
    if ln + 3 >= lnn and lnn != all_l:
        print(f'{m[:len(m) - (ln - lnn + 3)]}...')
        break
    else:
        print(m)

if __name__ == "__main__":
    main()


