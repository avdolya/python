def main():
    ...


a = int(input())
b = int(input())
width = len(str(a * b)) 
for i in range(1, a + 1):
    for j in range(1, b + 1):
        if j % 2 == 0:
            print(f"{j * a - i + 1:>{width}}", end=' ')
        else:
            print(f"{i + a * (j - 1):>{width}}", end=' ')
    print()
if __name__ == "__main__":
    main()