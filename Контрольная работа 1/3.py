n = int(input())
m = int(input())
st = []
for i in range(n, m - 1, -((n - m) // 3)):
    st.append(str(i))
print('; '.join(st))
