def main():
    ...


n = int(input())
name = input()
mn = name
for i in range(n - 1):
    name = input()
    if name < mn:
        mn = name
    else:
        ...
print(mn)
if __name__ == "__main__":
    main()