def main():
    ...


a = input().split()
b = input().split()
for i in (list(zip(a, b))):
    print(f'{i[0].replace(',', '')} - {i[1].replace(',', '')}')
if __name__ == "__main__":
    main()