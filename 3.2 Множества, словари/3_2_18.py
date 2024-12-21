dict = {}
mx = 0
for i in range(n := int(input())):
    x, y = input().split()
    index = (int(x) // 10, int(y) // 10)
    dict[index] = dict.get(index, 0) + 1
for i in dict:
    mx = max(mx, dict[i])
print(mx)
