def main():
    ...


a = int(input())
st = ""
for i in range(1, a + 1):
    for j in range(1,a + 1):
        st += str(i * j) + " "
    print(st)
    st = ""
if __name__ == "__main__":
    main()