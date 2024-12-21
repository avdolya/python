from itertools import product


def main():
    ...


a = int(input())
b = list(product([i for i in range(1,a - 1)],[j for j in range(1,a - 1)], [y for y in range(1,a - 1)]))
print('А Б В')
for i in b:
    if i[0] + i[1] + i[2] == a:
        print(f'{i[0]} {i[1]} {i[2]}')

if __name__ == "__main__":
    main()