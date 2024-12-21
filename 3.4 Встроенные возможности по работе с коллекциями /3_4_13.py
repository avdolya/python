from itertools import permutations


def main():
    ...


arr = []
for i in range(a := int(input())):
    arr.append(input())
arr.sort()
values = list(permutations(arr))
for value in values:
    print(', '.join(value))
if __name__ == "__main__":
    main()