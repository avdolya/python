from itertools import product


def main():
    ...


st = ''
a = int(input())
b = list(product([i for i in range(1, a + 1)], [j for j in range(1, a + 1)]))
for i in b:
    st += str(i[0] * i[1]) + ' '
    if st.count(' ') == a:
        print(st)
        st = ''
if __name__ == "__main__":
    main()