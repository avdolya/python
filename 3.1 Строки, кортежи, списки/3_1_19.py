def main():
    ...


a = input().split()
arr = []
for i in a:
    if i == '+':
        b = arr.pop()
        a = arr.pop()
        arr.append(a + b)
    elif i == '-':
        b = arr.pop()
        a = arr.pop()
        arr.append(a - b)
    elif i == '*':
        b = arr.pop()
        a = arr.pop()
        arr.append(a * b) 
    else:
        arr.append(int(i))
result = arr.pop()
print(result)
if __name__ == "__main__":
    main()