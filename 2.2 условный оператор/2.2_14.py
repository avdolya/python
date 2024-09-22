def main():
    pass
s = input()
a = min(s[0], s[1], s[2])
b = str(int(s[0]) + int(s[1]) + int(s[2]) - int(min(s[0], s[1], s[2])) - int(max(s[0], s[1], s[2])))
c = max(s[0], s[1], s[2])
if a == '0':
    first = b + a
    second = c + b
else:
    first = a + b
    second = c + b
print(first, second)
if __name__ == '__main__':
    main()

