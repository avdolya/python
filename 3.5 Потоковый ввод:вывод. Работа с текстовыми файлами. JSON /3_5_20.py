with open("numbers.num", "rb") as file:
    d = file.read()
res = 0
for i in range(0, len(d), 2):
    res += int.from_bytes(d[i: i + 2], "big")
res = res % 2**16
print(res)
