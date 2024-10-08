import math


def main():
    ...


n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
res = math.gcd(arr[0], arr[1])
for i in range(2, len(arr)):
    res = math.gcd(arr[i], res)
print(res)
if __name__ == "__main__":
    main()
    

