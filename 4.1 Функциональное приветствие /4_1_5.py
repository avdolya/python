def split_numbers(a):
    return tuple(map(int, a.split()))
print(split_numbers("1 2 3 4 5"))