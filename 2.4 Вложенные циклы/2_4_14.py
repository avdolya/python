def main():
    ...


a = int(input())
b = int(input())
numbers = []
width = len(str(a * b)) 
for i in range(1, a + 1):
    for j in range(1, b + 1):
        if i % 2 == 0:
            numbers.append(j + (i - 1) * b)
        if i % 2 != 0:
            print(f"{j + (i - 1) * b:>{width}}", end=' ') 
    if i % 2 == 0:
        for x in range(len(numbers) - 1, -1, -1):
            print(f"{numbers[x]:>{width}}", end=' ')
        numbers = []
    print() 
if __name__ == "__main__":
    main()
