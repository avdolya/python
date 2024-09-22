def main():
    pass
a = input()
b = input()
c = a + b
mx = max(int(c[0]), int(c[1]), int(c[2]), int(c[3]))
mn = min(int(c[0]), int(c[1]), int(c[2]), int(c[3]))
sr = int(c[0]) + int(c[1]) + int(c[2]) + int(c[3]) - mx - mn
if sr > 9:
    print(str(mx) + str(sr % 10) + str(mn))
else:
    print(str(mx) + str(sr) + str(mn))
if __name__ == '__main__':
    main()
