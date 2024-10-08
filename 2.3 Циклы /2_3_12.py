def main():
    ...


mx = 0
a = str(input())
for i in range(len(a)):
    mx = max(mx, int(a[i]))
print(mx)
if __name__ == "__main__":
    main()