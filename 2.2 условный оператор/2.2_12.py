def main():
    pass
a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')
if __name__ == '__main__':
    main()
