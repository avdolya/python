def main():
    pass
a = int(input())
b = int(input())
c = int(input())
if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
    print('100%')
elif max(a, b, c) ** 2 < (min(a, b, c)) ** 2 + (a + b + c - max(a, b, c) - min(a, b, c)) ** 2:
    print('крайне мала')
else:
    print('велика')

if __name__ == '__main__':
    main()
