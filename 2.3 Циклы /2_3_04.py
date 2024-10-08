def main():
    ...


st = ''
nach = int(input())
kon = int(input())
if nach < kon:
    for i in range(nach, kon + 1, 1):
        st += str(i) + ' '
    print(st)
else:
    for i in range(nach, kon - 1, -1):
        st += str(i) + ' '
    print(st)

if __name__ == '__main__':
    main()
