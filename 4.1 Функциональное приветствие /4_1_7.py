def can_eat(a, b):
    if sorted([abs(b[0] - a[0]), abs(b[1] - a[1])]) == [1, 2]:
        return True
    else:
        return False
print(can_eat((2, 1), (4, 2)))

        