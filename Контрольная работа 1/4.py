n = int(input())
a = int(input())
pred = a
arr = []
for i in range(n - 1):
    a = int(input())
    if a > pred:
        arr.append(a)
    pred = a
print(min(arr))
