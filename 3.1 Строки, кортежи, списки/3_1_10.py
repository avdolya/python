def main():
    ...


st = a = ''
mx = 0
ind = ''
while a != 'финиш':
    a = input().lower()
    if a == 'финиш':
        break
    else:
        st += a
st = st.replace(' ', '')
for i in st:
    if st.count(i) > mx:
        ind = i
        mx = st.count(i)
    if st.count(i) == mx:
        if ind > i:
            ind = i
print(ind)
if __name__ == "__main__":
    main()
