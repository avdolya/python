def main():
    ...


otv = 0
a = int(input())
b = int(input())
mx = 0
for i in range(1, a * b + 1):
    if i % a == 0 and i % b == 0:
        otv = i
        break 
print(otv)
if __name__ == "__main__":
    main()