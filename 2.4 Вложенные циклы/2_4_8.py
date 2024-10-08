def main():
    ...


mx = 0
res = ''
n = int(input())
for i in range(n):
    name = input()
    a = input()
    if mx <= sum(map(int, a)):
        res = name
        mx = sum(map(int, a))
print(res)
if __name__ == "__main__":
    main()
    