def main():
    ...


name = ''
k = sm = 0
a = int(input())
for i in range(a):
    while name != 'ВСЁ':
        name = input()
        if name == 'зайка':
            k = 1
    name = ''
    if k == 1:
        sm += 1
        k = 0
print(sm)
if __name__ == "__main__":
    main()