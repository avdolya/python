def main():
    pass
a = input()
b = input()
c = input()
if 'зайка' in min(a, b, c):
    print(min(a, b, c), len(min(a, b, c)))
elif a != min(a, b, c) and a != max(a, b, c) and 'зайка' in a:
    print(a, len(a))
elif b != min(a, b, c) and b != max(a, b, c) and 'зайка' in b:
    print(b, len(b))
elif c != min(a, b, c) and c != max(a, b, c) and 'зайка' in c:
    print(c, len(c))
elif 'зайка' in max(a, b, c):
    print(max(a, b, c), len(max(a, b, c)))
if __name__ == '__main__':
    main()
