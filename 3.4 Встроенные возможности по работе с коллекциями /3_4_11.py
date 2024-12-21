from itertools import product


def main():
    ...


a = int(input())
b = int(input())
k = 0
values = list(product([i for i in range(1, a + 1)], [j for j in range(1, b + 1)]))
for value in values:
    if value[1] == b:
        print(f"{value[1] + (value[0] - 1) * b:>{len(str(a * b))}}", end=' ')
        print()
    else:
        print(f"{value[1] + (value[0] - 1) * b:>{len(str(a * b))}}", end=' ')
if __name__ == "__main__":
    main()
