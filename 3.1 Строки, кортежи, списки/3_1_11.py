def main():
    ...


arr = []
for i in range(int(input())):
    a = input()
    arr.append(a)
m = input()
m = m.lower()
for i in range(len(arr)):
    if m in arr[i].lower():
        print(arr[i])
if __name__ == "__main__":
    main()