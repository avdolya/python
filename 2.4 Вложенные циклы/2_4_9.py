def main():
    ...


sm = ''
n = int(input())
for i in range(n):
    a = input()
    sm += str(max(map(int, a)))
print(sm)
if __name__ == "__main__":
    main()
    