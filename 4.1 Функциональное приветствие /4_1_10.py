def merge(a, b):
    s = list(a + b)
    arr = []
    while s != []:
        arr.append(min(s))
        s.remove(min(s))
    return tuple(arr)
print(merge((7, 12), (1, 9, 50)))
