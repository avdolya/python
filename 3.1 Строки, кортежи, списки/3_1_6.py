def main():
    ...


sm = 0
for i in range(n := int(input())):
    a = input()
    sm += a.count('зайка')
print(sm)
if __name__ == "__main__":
    main()