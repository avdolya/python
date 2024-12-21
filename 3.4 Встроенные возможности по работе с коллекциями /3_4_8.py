from itertools import cycle


def main():
    ...


arr = []
k = 0
n = int(input())
arr = [input() for i in range(n)]
days = int(input())
for i in cycle(arr):
    if k < days:
        print(i)
        k += 1
    else:
        break
if __name__ == "__main__":
    main()