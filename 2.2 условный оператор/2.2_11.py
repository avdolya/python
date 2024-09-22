def main():
    pass
a = input()
sm = int(a[0]) + int(a[1]) + int(a[2])
mx = int(max(a[0], a[1], a[2]))
mn = int(min(a[0], a[1], a[2]))
if mn + mx == 2 * (sm - mx - mn):
    print('YES')
else:
    print('NO')

if __name__ == '__main__':
    main()
