def main():
    ...


a = int(input())
width = int(input())
arr = []
for i in range(1, a + 1):
    for j in range(1, a + 1):
        arr.append(i * j)
    for x in range(len(arr)):
        if x == len(arr) - 1:
            print(f"{arr[x]:^{width}}")
        else:
            print(f"{arr[x]:^{width}}", end="|") 
    arr = []
    if i != a:
        print((a * (width + 1) - 1) * '-')
if __name__ == "__main__":
    main()

