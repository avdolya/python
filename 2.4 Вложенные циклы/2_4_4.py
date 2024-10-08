def main():
    ...


sm = 0
a = int(input())
for i in range(a):
    b = input()
    sm += sum(map(int, b))
print(sm)
if __name__ == "__main__":
    main()