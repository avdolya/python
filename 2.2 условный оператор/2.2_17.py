def main():
    pass
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if a == 0:
    if b != 0 and c != 0:
        print("{:.2f}".format(((-1) * c) / b))
    if b == 0 and c == 0:
        print("Infinite solutions")
    if b == 0 and c != 0:
        print('No solution')
    if b != 0 and c == 0:
        print(0)
else:
    if d == 0:
        x1 = (-b) / (2 * a)
        print("{:.2f}".format(x1))
    if d > 0:
        x2 = (-b + d ** 0.5) / (2 * a)
        x1 = (-b - d ** 0.5) / (2 * a)
        print("{:.2f}".format(min(x1, x2)), "{:.2f}".format(max(x1, x2)))
    if d < 0:
        print('No solution')
if __name__ == '__main__':
    main()
