def is_prime(x):
    a = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            a.append(i)
            a.append(x // i)
    if len(a) == 2:
        return True
    else:
        return False
print(is_prime(79701))