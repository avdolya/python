def main():
    ...


a = input().lower().replace(' ', '')
if a == a[::-1].replace(' ', ''):
    print('YES')
else:
    print('NO')
if __name__ == "__main__":
    main()


