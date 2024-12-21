def main():
    ...


a = input().split()
for index, value in enumerate(a, 1):
    print(f'{index}. {value}')
if __name__ == "__main__":
    main()