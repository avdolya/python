def main():
    ...


a = int(input())
b = int(input())
mx = 0
for i in range(1, min(a, b)):
    if a % i == 0 and b % i == 0:
        mx = max(i, mx) 
print(mx)
if __name__ == "__main__":
    main()