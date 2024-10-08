def main():
    ...


def prost(a):
    arr = []
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            arr.append(i)
            arr.append(a // i)
    arr.sort()
    if arr[0] == 1 and arr[1] == a and len(arr) == 2 and a != 1:
        return 1
    else:
        return 0
    

k = 0
n = int(input())
for i in range(n):
    a = int(input())
    if prost(a) == 1:
        k += 1
print(k)
if __name__ == "__main__":
    main()