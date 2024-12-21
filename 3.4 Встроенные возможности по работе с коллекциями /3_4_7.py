from itertools import combinations


def main():
    ...


arr = []
n = int(input())
arr = [input() for i in range(n)]
values = list((combinations(arr, 2)))
for value in values:
    print(f'{value[0]} - {value[1]}')
if __name__ == "__main__":
    main()