def main():
    ...


st = ''
width = w = 0
n = int(input())
for i in range(n):
    for j in range(n):
        w = max(w, min(j + 1, n - i, i + 1, n - j))
width = len(str(w))
for i in range(n):
    for j in range(n):
        print(f"{str(min(j + 1, n - i, i + 1, n - j)):>{width}}", end=' ') 
    print()
    st = ''
if __name__ == "__main__":
    main()