import math
def main():
    ...


a = input().split(' ')
n = math.gcd(int(a[0]), int(a[1]))
for i in range(2, len(a)):
    n = math.gcd(int(a[i]), n)
print(n)
if __name__ == "__main__":
    main()