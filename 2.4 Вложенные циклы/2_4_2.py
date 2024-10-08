def main():
    ...

    
a = int(input())
for i in range(1, a + 1):
    for j in range(1,a + 1):
        print(f'{j} * {i} = {i * j}')
if __name__ == "__main__":
    main()