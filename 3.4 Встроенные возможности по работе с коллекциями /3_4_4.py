def main():
    ...


st = ''
a = input().split()
for i in range(len(a)):
    for j in a[:i + 1]:
        st += j + ' '
    print(st)
    st = ''
if __name__ == "__main__":
    main()