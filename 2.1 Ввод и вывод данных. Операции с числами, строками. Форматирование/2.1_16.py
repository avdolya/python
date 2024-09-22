def main():
    pass
a = int(input())
b = int(input())
c = int(input())
res = round((b - a) / c, 2)
if len(str(res)) == 3:
    print(f"{res}0")
else:
    print(res)
if __name__ == '__main__':
    main()
