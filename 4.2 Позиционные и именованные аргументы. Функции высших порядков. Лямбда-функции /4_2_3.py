def gсd(*values):
    arr = [value for value in values]
    mn = min(arr)
    k = False
    cnt = 0
    while not k:
        for i in arr:
            if i % mn == 0:
                cnt += 1
        if cnt == len(arr):
            k = True
        else:
            k = False
            mn -= 1
        cnt = 0
    return mn
print(gсd(36, 48, 156, 100500))
