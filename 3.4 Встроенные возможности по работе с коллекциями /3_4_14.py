from itertools import permutations


def main():
    ...


arr = []
for i in range(a := int(input())):
    arr.append(input())
arr.sort()
for value in permutations(arr,3):
    print(','.join(value))
if __name__ == "__main__":
    main()