def make_linear(arr):
    result = []
    for i in arr:
        if type(i) is list:
            result.extend(make_linear(i))
        else:
            result.append(i)
    return result