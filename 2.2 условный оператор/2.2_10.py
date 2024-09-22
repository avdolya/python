def main():
    pass
a = input()
f = int(a[2]) + int(a[1])
s = int(a[0]) + int(a[1])
if max(f, s) == f:
    print(str(f) + str(s))
else:
    print(str(s) + str(f))
if __name__ == '__main__':
    main()
