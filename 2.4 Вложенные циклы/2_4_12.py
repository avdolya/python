def main():
    ...


a = int(input())
b = int(input())
width = len(str(a * b)) 
for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(f"{j + (i - 1) * b:>{width}}", end=' ')
    print()
   
if __name__ == "__main__":
    main()

