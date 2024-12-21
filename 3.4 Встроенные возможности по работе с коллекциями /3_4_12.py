def main():
    ...


a = []
for i in range(n := int(input())):
    a += input().split(', ')
    a.sort()

for index, value in enumerate(a, 1):
    print(f'{index}. {value}')
if __name__ == "__main__":
    main()