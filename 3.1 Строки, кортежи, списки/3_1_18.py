def main():
    ...


k = 1
a = input()
number = a[0]
for i in range(1, len(a)):
    if a[i] == number:
        k += 1
    else:
        print(number, k)
        number = a[i]
        k = 1
print(number, k)

if __name__ == "__main__":
    main()
